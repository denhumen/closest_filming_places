"""
Module is developed
to create html map-file
with input location and
the closest filming places
"""
import argparse
from functools import lru_cache
import os
import re
from typing import List, Tuple
import folium as fl
from geopy.distance import geodesic
from geopy.geocoders import Nominatim

parser = argparse.ArgumentParser(description="Find the closest filming places")
parser.add_argument('latitude', type=str, help="Custom latitude")
parser.add_argument('longitude', type=str, help="Custom longitude")
parser.add_argument('path', type=str, help="Path to the dataset")
args = parser.parse_args()

def read_list(path: str) -> List[str]:
    """
    Fucntion reads .list file
    and returns list with 

    Args:
        path: str - path to the .list file
    Returns:
        films: List[str] - list of films and filming places
    """
    with open(path, mode='r', encoding='latin1', errors='ignore') as file:
        data = file.read().splitlines()
    if len(data) > 10000:
        data = data[0:10000]
    years = ["(" + str(year) + ")" for year in range(1970, 2023)]
    films = []
    for line in data:
        if any(year in line for year in years):
            films.append(line)
    for index, film in enumerate(films):
        films[index] = [x for x in film.split('\t') if x != '']
    return films

@lru_cache(maxsize=None)
def get_cords_of_the_place(city: str) -> Tuple[int, int]:
    """
    Function finds map cordinates
    of the ciry given

    Args:
        city: str - name of the city(ex: Hyderabad)
    Returns:
        location: Tuple[int, int] - tuple with cords
    of the city, First - latitude, second - longitude
    """
    try:
        geolocator = Nominatim(user_agent="Maps.app")
        location = geolocator.geocode(city)
        return location.latitude, location.longitude
    except Exception:
        return None

def create_map(x: int, y: int, films: List[Tuple[str, Tuple[int, int], int]]):
    """
    Function creates map with
    input location

    Args:
        x: int - latitude
        y: int - longitude
    """
    try:
        map = fl.Map(location=[x, y], zoom_start=7, tiles="Stamen Toner")
        map.add_child(fl.Marker(location=[x, y],
                            popup="Your input coords",
                            icon=fl.Icon(color='lightgray', icon='home', prefix='fa')))
        for film in films:
            name, coords, _ = film
            map.add_child(fl.Marker(location=[coords[0], coords[1]],
                            popup=re.findall('".+"', name)[0][1:-1],
                            icon=fl.Icon(color='red', icon='film', prefix='fa')))
        map_name = "Map.html"
        map.save(map_name)
        os.startfile(os.getcwd() + '\\' + map_name)
    except ZeroDivisionError:
        print("Something went wrong")

def find_distance_between_two_places(cords1: Tuple[int, int],
                                     cords2: Tuple[int, int]) -> int:
    """
    Function finds the distance
    between two points on a map
    based on latitude/longitude

    Args:
        cords1: Tuple[int, int] - coordinates of the first place
        cords2: Tuple[int, int] - coordinates of the second place
    Returns:
        distance: int - distance between two points
    """
    return geodesic(cords1, cords2).km

def get_distances_between_enter_point_and_film_points(enter_coords: Tuple[int, int], films: List[List[str]]):
    """
    Function finds distances between
    enter coordinates and film coordinates
    and finds the closest places

    Args:
        enter_coords: Tuple[int, int] - user coords
        filns: List[List[str]] - films list got from database
    Returns:
        dist_films: List[Tuple[str, Tuple[int, int], int]] - list with film
    distances, names and coords
    """
    dist_films = []
    used_locations = set()
    or_films = []
    for film in films:
        if film[1].strip() in used_locations:
            continue
        or_films.append(film)
        used_locations.add(film[1].strip())
    counter = 0
    for film in or_films:
        try:
            coords = get_cords_of_the_place(film[1].strip())
            if coords == None:
                continue
        except Exception:
            continue
        distance = find_distance_between_two_places(enter_coords, coords)
        if distance < 1000:
            dist_films.append((film[0], coords, distance))
            if len(dist_films) >= 10:
                break
    return dist_films

if __name__ == "__main__":
    enter_coords = (args.latitude, args.longitude)
    films = read_list(args.path)
    dist_films = get_distances_between_enter_point_and_film_points(enter_coords, films)
    create_map(args.latitude, args.longitude, dist_films)
