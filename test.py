import unittest
from weather_api import WeatherAPI
from database import create_database, get_session, insert_data, query_data

# D - Create a unit test file named test.py that executes three tests run against your code.
class TestWeatherAPI(unittest.TestCase):
    """
    Test case for the fetch_temperature_data function in the WeatherAPI class.
    """
    def test_fetch_temperature_data(self):
        """
        Ensure the fetch_temperature_data function retrieves valid weather data successfully.
        """
        weather_api = WeatherAPI(latitude=36.569135, longitude=-82.197489)  # Bristol, Tennessee
        month = 2
        day = 28
        event_year = 2025

        data = weather_api.fetch_temperature_data(month, day, event_year)
        self.assertIsNotNone(data)


class TestDatabase(unittest.TestCase):
    """
    Test case for the insert_data function in database.py.
    """
    def test_insert_data(self):
        """
        Ensure the insert_data function inserts data into the database successfully.
        Query the data using the query_data function.
        """
        engine = create_database()
        session = get_session(engine)

        latitude = 36.569135
        longitude = -82.197489
        month = 2
        day = 28
        year = 2023
        avg_temp = 40.0
        min_temp = 30.0
        max_temp = 50.0
        avg_wind_speed = 5.0
        min_wind_speed = 0.0
        max_wind_speed = 10.0
        sum_precipitation = 1.0
        min_precipitation = 0.0
        max_precipitation = 2.0

        insert_data(session, latitude, longitude, month, day, year, avg_temp, min_temp, max_temp,
                    avg_wind_speed, min_wind_speed, max_wind_speed, sum_precipitation,
                    min_precipitation, max_precipitation)

        data = query_data(engine, latitude, longitude, month, day, year)
        self.assertEqual(len(data), 1)

class TestInitialization(unittest.TestCase):
    """
    Test case for initializing the WeatherAPI class.
    """
    def test_initialization(self):
        """
        Ensure the WeatherAPI class initializes correctly.
        """
        latitude = 36.569135
        longitude = -82.197489
        weather_api = WeatherAPI(latitude, longitude)

        self.assertEqual(weather_api.latitude, latitude)
        self.assertEqual(weather_api.longitude, longitude)

if __name__ == '__main__':
    unittest.main()