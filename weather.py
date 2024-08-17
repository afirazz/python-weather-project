import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    iso_date = datetime.fromisoformat(iso_string)

    formatted_date = iso_date.strftime("%A %d %B %Y")

    return formatted_date


def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """

    temp_in_fahrenheit = float(temp_in_fahrenheit)
    temp_in_celcius = (temp_in_fahrenheit - 32) * 5/9
    temp_in_celcius_rounded = float("%.1f" % temp_in_celcius)

    return temp_in_celcius_rounded

def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    weather_data_float = [float(value) for value in weather_data]

    weather_data = weather_data_float 

    total = 0

    for index in range(len(weather_data)):
        total = total + weather_data[index]
    
    mean = total / len(weather_data)

    return mean

def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    csv_list = []

    with open(csv_file) as file:
        csv_reader = csv.reader(file)
        next(csv_reader)

        for row in csv_reader:
            if row:
                csv_list.append([row[0], float(row[1]), float(row[2])])

    return csv_list


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    weather_data_float = [float(value) for value in weather_data]

    weather_data = weather_data_float 
    
    try:
        min_value = weather_data[0]
    except:
        return ()
    
    min_position = 0

    for index, value in enumerate(weather_data):
        if value < min_value:
            min_value = value
            min_position = index
        elif value == min_value:
            min_position = index

    return min_value, min_position

def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    weather_data_float = [float(value) for value in weather_data]

    weather_data = weather_data_float 
    
    try:
        max_value = weather_data[0]
    except:
        return ()
    
    max_position = 0

    for index, value in enumerate(weather_data):
        if value > max_value:
            max_value = value
            max_position = index
        elif value == max_value:
            max_position = index

    return max_value, max_position

def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
