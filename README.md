# Map with closest filming places
This is a Python script that creates a map with the closest places from a database to the input place. The input latitude and longitude are used to search for the nearest places in the database, and these places are displayed on a map using the Folium library.

Prerequisites
In order to use this script, you will need to have the following installed:

 - Python3
 - Folium

## Usage
To use this script, follow these steps:

 1. Clone the repository to your local machine.

 2. Open a terminal and navigate to the directory where the repository is located.

 3. Ensure that you have the required dependencies installed (see Prerequisites).

 4. Run the script using the following command:

```css
python main.py <latitude> <longitude> <path_to_dataset>
```

 5. Replace <latitude>, <longitude>, <path_to_dataset> with the latitude and longitude of the input place and the path to your dataset, where script will get filming positions(the example file you can see directly in the repository and it must have .list extension), respectively.

The script will generate a map in your default web browser showing the closest places to the input location.

### Example

Using folowing command in the cmd
```css
python main.py <longitude> <path_to_dataset>
```
We get this map:

## Configuration
 
The script reads the database configuration from a config.json file. The following properties can be configured:

 - **database**: the name of the database file.
 - **table**: the name of the table containing the places.
 - **name_column**: the name of the column containing the name of the place.
 - **lat_column**: the name of the column containing the latitude of the place.
 - **lon_column**: the name of the column containing the longitude of the place.

 
## Contributing
If you find a bug or have a feature request, please create an issue on the GitHub repository.

If you would like to contribute to the project, please fork the repository and create a pull request with your changes.

## License
This script is released under the MIT License. See the LICENSE file for more information.
