import requests

class WeatherAPI:
    def __init__(self, latitude, longitude):
        """
        Initialize the WeatherAPI instance.

        Args:
            latitude (float): Latitude of the event location.
            longitude (float): Longitude of the event location.
        """
        self.latitude = latitude
        self.longitude = longitude
        self.base_url = "https://archive-api.open-meteo.com/v1/archive"

    # C2 - Pull the mean temperature data in Fahrenheit for the event location and date for the most recent five years.
    def fetch_temperature_data(self, month, day, event_year):
        """
        Fetch the mean temperature data in Fahrenheit for the event location and date for the most recent five years.

        Args:
            month (int): Month of the event.
            day (int): Day of the event.
            event_year (int): The year from which to calculate the previous five years.

        Returns:
            float: Mean temperature in Fahrenheit for the most recent five years.
        """
        temperature_data = []

        for year in range(event_year - 5, event_year):
            date = f"{year}-{month:02d}-{day:02d}"

            params = {
                "latitude": self.latitude,
                "longitude": self.longitude,
                "start_date": date,
                "end_date": date,
                "temperature_unit": "fahrenheit",
                "daily": "temperature_2m_mean"
            }

            response = requests.get(self.base_url, params=params)

            if response.status_code == 200:
                data = response.json()
                if "daily" in data and "temperature_2m_mean" in data["daily"]:
                    mean_temp = data["daily"]["temperature_2m_mean"][0]
                    temperature_data.append(mean_temp)
            else:
                print(f"Error: {response.status_code}")

        if temperature_data:
            return sum(temperature_data) / len(temperature_data)
        return None

    # C2 - Pull the maximum wind speed in miles per hour for the event location and date for the most recent five years.
    def fetch_wind_speed_data(self, month, day, event_year):
        """
        Fetch the maximum wind speed data in m/s for the event location and date for the most recent five years.

        Args:
            month (int): Month of the event.
            day (int): Day of the event.
            event_year (int): The year from which to calculate the previous five years.

        Returns:
            float: Maximum wind speed in m/s for the most recent five years.
        """
        wind_speed_data = []

        for year in range(event_year - 5, event_year):
            date = f"{year}-{month:02d}-{day:02d}"

            params = {
                "latitude": self.latitude,
                "longitude": self.longitude,
                "start_date": date,
                "end_date": date,
                "daily": "wind_speed_10m_max"
            }

            response = requests.get(self.base_url, params=params)

            if response.status_code == 200:
                data = response.json()
                if "daily" in data and "wind_speed_10m_max" in data["daily"]:
                    max_wind_speed = data["daily"]["wind_speed_10m_max"][0]
                    wind_speed_data.append(max_wind_speed)
            else:
                print(f"Failed to fetch data for {date}: {response.status_code}")

        if wind_speed_data:
            return sum(wind_speed_data) / len(wind_speed_data)
        return None

    # C2 - Pull the precipitation sum in inches for the event location and date for the most recent five years.
    def fetch_precipitation_data(self, month, day, event_year):
        """
        Fetch the sum of precipitation data in mm for the event location and date for the most recent five years.

        Args:
            month (int): Month of the event.
            day (int): Day of the event.
            event_year (int): The year from which to calculate the previous five years.

        Returns:
            float: Total precipitation in mm for the most recent five years.
        """
        precipitation_data = []

        for year in range(event_year - 5, event_year):
            date = f"{year}-{month:02d}-{day:02d}"

            params = {
                "latitude": self.latitude,
                "longitude": self.longitude,
                "start_date": date,
                "end_date": date,
                "daily": "precipitation_sum"
            }

            response = requests.get(self.base_url, params=params)

            if response.status_code == 200:
                data = response.json()
                if "daily" in data and "precipitation_sum" in data["daily"]:
                    total_precipitation = data["daily"]["precipitation_sum"][0]
                    precipitation_data.append(total_precipitation)
            else:
                print(f"Failed to fetch data for {date}: {response.status_code}")

        if precipitation_data:
            return sum(precipitation_data) / len(precipitation_data)
        return None