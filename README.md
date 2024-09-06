# Weather API Program

## Overview
This program fetches weather data, such as temperature, wind speed, and precipitation, for the provided event location and date over the past five year and then stores the information in a SQLite database, and provides methods to query and display the stored data.

## Technologies Used
- **Python#**: Programming language for used for the program.
- **Requests**: Used to make HTTP requests to the Open-Meteo API.
- **SQLAlchemy**: ORM (Object-Relational Mapper) used for interacting with the SQLite database.
- **SQLite**: Local database to store weather data.
- **UnitTest**: Python's built-in testing framework used for unit testing.
- **MVVM Architecture**: Organizing app structure.

## Skills Demonstrated
- **Database Design**: Storing weather data in a local SQLite database using SQLAlchemy.
- **Unit Testing**: Writing and running unit tests to validate program functionality.
- **API Integration**: Connecting to external API services.
- **JSON Parsing**: Extracting data from API responses.

## Features
- **Weather Data Fetching**: Gathers weather data, including average temperature, maximum wind speed, and total precipitation for a specific location and date for the past five years.
- **SQLite Database**: Stores weather data in a local SQLite database using SQLAlchemy.
- **Query Functionality**: Allows users to query the stored weather data and print it to the console.
- **Unit Testing**: Includes tests to ensure the accuracy of data fetching, database insertion, and object initialization.

## Project Structure
- main.py: This is the main script to run the program.
- weather_api.py: Contains the code that fetches data from the API.
- weather_variables.py: Contains the WeatherVariables class.
- database.py: Contains the code for creating and querying the database, as well as inserting data.
- test.py: Contains unit tests for the program.
- requirements.txt: Provides a list of the required packages, including versions.

## Program Requirements
- Python 3.6 or newer
- Packages listed in requirements.txt, which include:
  - requests==2.32.3
  - SQLAlchemy==2.0.25

You can install the packages listed in requirements.txt by running this command in the terminal:
```
pip install -r requirements.txt
```

## How to Run the Program
1. Clone/download the repository.
2. Review the program requirements and install the required packages if needed.
3. Set the event location and date in main.py by assigning the appropriate values to the latitude, longitude, month, day, and event_year variables.
4. Run the main.py script to retrieve, store, and query the weather data for the last five years. The data will be printed to the console.

```
python main.py
```

## Testing the Program
You can run the unit tests for the program by running this command in the terminal:
```
python -m unittest test.py
```