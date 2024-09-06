from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a base class
Base = declarative_base()

# C4 - Create a table in SQLite using the SQLAlchemy ORM module.
class WeatherData(Base):
    """
    Defines the structure of the weather data table in SQLite.

    Attributes:
        __tablename__ (str): Table name.
        id (int): Primary key.
        latitude (float): Latitude of event location.
        longitude (float): Longitude of event location.
        month (int): Month of data.
        day (int): Day of data.
        year (int): Year of data.
        avg_temp (float): Average temperature.
        min_temp (float): Minimum temperature.
        max_temp (float): Maximum temperature.
        avg_wind_speed (float): Average wind speed.
        min_wind_speed (float): Minimum wind speed.
        max_wind_speed (float): Maximum wind speed.
        sum_precipitation (float): Total precipitation.
        min_precipitation (float): Minimum precipitation.
        max_precipitation (float): Maximum precipitation.
    """
    __tablename__ = 'weather'
    id = Column(Integer, primary_key=True, autoincrement=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    month = Column(Integer, nullable=False)
    day = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)
    avg_temp = Column(Float, nullable=True)
    min_temp = Column(Float, nullable=True)
    max_temp = Column(Float, nullable=True)
    avg_wind_speed = Column(Float, nullable=True)
    min_wind_speed = Column(Float, nullable=True)
    max_wind_speed = Column(Float, nullable=True)
    sum_precipitation = Column(Float, nullable=True)
    min_precipitation = Column(Float, nullable=True)
    max_precipitation = Column(Float, nullable=True)

# C4 - Create a table in SQLite using the SQLAlchemy ORM module.
def create_database():
    """
    Create the database, including the weather table.

    Returns:
        Engine: SQLAlchemy engine connected to the database.
    """
    engine = create_engine('sqlite:///weather.db')
    Base.metadata.create_all(engine)
    return engine

def get_session(engine):
    """
    Creates a SQLAlchemy session bound to the engine.

    Args:
        engine (Engine): The engine being bound to the session.

    Returns:
        Session: SQLAlchemy session.
    """
    Session = sessionmaker(bind=engine)
    return Session()

# C5 - Populate the table created in part C4 with the weather data for your chosen location and date.
def insert_data(session, latitude, longitude, month, day, year, avg_temp, min_temp, max_temp, avg_wind_speed,
                min_wind_speed, max_wind_speed, sum_precipitation, min_precipitation, max_precipitation):
    """
    Inserts data into the weather table.

    Args:
        session (Session): SQLAlchemy session object.
        latitude (float): Latitude of the event location.
        longitude (float): Longitude of the event location.
        month (int): Month of data.
        day (int): Day of data.
        year (int): Year of data.
        avg_temp (float): Average temperature.
        min_temp (float): Minimum temperature.
        max_temp (float): Maximum temperature.
        avg_wind_speed (float): Average wind speed.
        min_wind_speed (float): Minimum wind speed.
        max_wind_speed (float): Maximum wind speed.
        sum_precipitation (float): Total precipitation.
        min_precipitation (float): Minimum precipitation.
        max_precipitation (float): Maximum precipitation.
    """
    weather = WeatherData(
        latitude=latitude,
        longitude=longitude,
        month=month,
        day=day,
        year=year,
        avg_temp=avg_temp,
        min_temp=min_temp,
        max_temp=max_temp,
        avg_wind_speed=avg_wind_speed,
        min_wind_speed=min_wind_speed,
        max_wind_speed=max_wind_speed,
        sum_precipitation=sum_precipitation,
        min_precipitation=min_precipitation,
        max_precipitation=max_precipitation
    )

    session.add(weather)
    session.commit()

# Write a method that queries the table you created in SQLite and retrieves the data you stored in part C5.
def query_data(engine, latitude, longitude, month, day, year):
    """
    Queries the weather data table for records matching the provided criteria.

    Args:
        engine (Engine): SQLAlchemy engine.
        latitude (float): Latitude of the event location.
        longitude (float): Longitude of the event location.
        month (int): Month of the data.
        day (int): Day of the data.
        year (int): Year of the data.

    Returns:
        list: A list of objects that match the query criteria.
    """
    # Session creation
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query results or provide an error
    try:
        results = session.query(WeatherData).filter_by(
            latitude=latitude,
            longitude=longitude,
            month=month,
            day=day,
            year=year
        ).all()
    except SQLAlchemyError as e:
        print(f"An error occurred: {e}")
        results = []

    return results