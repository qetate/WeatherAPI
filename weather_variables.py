class WeatherVariables:
    def __init__(self, latitude, longitude, month, day, year):
        """
        C1 - Create a class with the instance variables for your chosen location and date.

        Args:
            latitude (float): Latitude of the location for the event.
            longitude (float): Longitude of the location for the event.
            month (int): Month of the event.
            day (int): Day of the event.
            year (int): Year of the event.
        """
        self.latitude = latitude
        self.longitude = longitude
        self.month = month
        self.day = day
        self.year = year
        self.avg_temp = None
        self.min_temp = None
        self.max_temp = None
        self.avg_wind_speed = None
        self.min_wind_speed = None
        self.max_wind_speed = None
        self.sum_precipitation = None
        self.min_precipitation = None
        self.max_precipitation = None