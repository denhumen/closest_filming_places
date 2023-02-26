# Map with closest filming places
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

This is a Python script that creates a map with the closest places from a database to the input place. The input latitude and longitude are used to search for the nearest places in the database, and these places are displayed on a map using the Folium library.

Prerequisites
In order to use this script, you will need to have the following installed:

 - Python3
 - Folium
 - Geopy

## Usage
To use this script, follow these steps:

 1. Clone the repository to your local machine.

 2. Open a terminal and navigate to the directory where the repository is located.

 3. Ensure that you have the required dependencies installed (see Prerequisites).

 4. Run the script main.py using the following command:

```css
python main.py <latitude> <longitude> <path_to_dataset>
```

 5. Replace <latitude>, <longitude>, <path_to_dataset> with the latitude and longitude of the input place and the path to your dataset, where script will get filming positions(the example file you can see directly in the repository and it must have .list extension), respectively.(as path_to_dataset you can use locations.list from this repo, there are given more than 10k filming locations)

The script will generate a map in your default web browser showing the closest places to the input location.

### Example

Using folowing command in the cmd
```css
python main.py 53.5 9.9 locations.list
```
We get this map:
 ![for git](https://user-images.githubusercontent.com/116521940/220355003-0b99f243-ca68-4a52-99fa-1fb4f1e228d1.png)

## Contributing
If you find a bug or have a feature request, please create an issue on the GitHub repository.

If you would like to contribute to the project, please fork the repository and create a pull request with your changes.

## License
This script is released under the MIT License. See the LICENSE file for more information.
