"""
Module is developed
to create html map-file
with input location and
the closest filming places
"""
import folium as fl
from typing import List, Tuple
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import argparse

parser = argparse.ArgumentParser(description="Find the closest filming places")
parser.add_argument('latitude', type=str, help="Custom latitude")
parser.add_argument('longitude', type=str, help="Custom longitude")
parser.add_argument('path', type=str, help="Path to the dataset")
group = parser.add_mutually_exclusive_group()
group.add_argument('--open', action='store_true', help='Open map file')
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
    pass

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
    pass

def create_map(x: int, y: int, films: List[Tuple[str, Tuple[int, int], int]]):
    """
    Function creates map with
    input location

    Args:
        x: int - latitude
        y: int - longitude
    """
    pass

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
    pass

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
    pass