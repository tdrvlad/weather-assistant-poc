import logging
from langchain.tools import tool
logging.getLogger().setLevel(logging.INFO)

# Make sure to provide intuitive naming and descriptions.
# This is how the LLM identifies the functions that can be called.
# Append all the defined tools to the `tools` list at the end of the script


@tool
def get_temperature_forecast(location: str) -> dict:
    """
    Get the temperature forecast for the current day and the next day at the specified location.
    :param location: string for the city for which the forecast is queried
    :return forecast: dictionary with forecast data
    """
    logging.info("LLM used tool `get_temperature_forecast`.")
    dummy_forecast = {
        'parameter': 'temperature',
        'unit': 'celsius degrees',
        'location': location,
        'today': 23,
        'tomorrow': 25
    }
    return dummy_forecast


@tool
def get_humidity_forecast(location: str) -> dict:
    """
    Get the relative humidity forecast for the current day and the next day at the specified location.
    :param location: string for the city for which the forecast is queried
    :return forecast: dictionary with forecast data
    """
    logging.info("LLM used tool `get_humidity_forecast`.")
    dummy_forecast = {
        'parameter': 'relative humidity',
        'unit': 'percentage',
        'location': location,
        'today': 54,
        'tomorrow': 67
    }
    return dummy_forecast


@tool
def get_location() -> str:
    """
    Get the current system location for the user.
    :return location: string specifying the user's current city.
    """
    logging.info("LLM used tool `get_location`.")
    city = 'Bucharest, Romania'
    return city