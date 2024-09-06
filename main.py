from weather_api import WeatherAPI
from weather_variables import WeatherVariables
from database import create_database, get_session, insert_data, query_data

def main():
    """
    Function to gather weather data for the event location and date for the past five years.
    """
    latitude = 47.6249
    longitude = -122.5210
    month = 10
    day = 31
    event_year = 2024

    # C3 - Create an instance of the class in C1 to call the methods used in C2 for the daily weather variables.
    weather_api = WeatherAPI(latitude, longitude)
    engine = create_database()
    session = get_session(engine)

    # C5 - Populate the table created in part C4 with the weather data for your chosen location and date.
    # Fetch and insert weather data for the last five years
    for year in range(event_year - 5, event_year):
        # C3 - Create an instance of the class in C1 to call the methods used in C2 for the daily weather variables.
        weather_variables = WeatherVariables(latitude, longitude, month, day, year)

        # Fetch weather data
        weather_variables.avg_temp = weather_api.fetch_temperature_data(month, day, year)
        weather_variables.max_wind_speed = weather_api.fetch_wind_speed_data(month, day, year)
        weather_variables.sum_precipitation = weather_api.fetch_precipitation_data(month, day, year)

        # Insert the data into the database
        insert_data(
            session,
            latitude,
            longitude,
            month,
            day,
            year,
            weather_variables.avg_temp,
            weather_variables.min_temp,
            weather_variables.max_temp,
            weather_variables.avg_wind_speed,
            weather_variables.min_wind_speed,
            weather_variables.max_wind_speed,
            weather_variables.sum_precipitation,
            weather_variables.min_precipitation,
            weather_variables.max_precipitation
        )

    # C6 - Write a method that queries the table you created in SQLite and retrieves the data you stored in part C5.
    for year in range(event_year - 5, event_year):
        results = query_data(engine, latitude, longitude, month, day, year)
        # Print retrieved data to console
        for result in results:
            print(f"\n{result.latitude}, {result.longitude} on {result.year}-{result.month:02d}-{result.day:02d}")
            print(f"Average Temp: {result.avg_temp:.2f}")
            print(f"Max Wind Speed: {result.max_wind_speed:.2f}")
            print(f"Sum Precipitation: {result.sum_precipitation:.2f}")

# Entry point
if __name__ == "__main__":
    main()