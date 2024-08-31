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
    temp_in_celcius_rounded = round(temp_in_celcius, 1)

    return temp_in_celcius_rounded

def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    weather_data_float = [float(value) for value in weather_data]
   
    mean = sum(weather_data_float) / len(weather_data_float)

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
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            if row: 
                csv_list.append([row["date"], float(row["min"]), float(row["max"])])

    return csv_list

def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    weather_data_float = [float(value) for value in weather_data]
    
    try:
        min_value = min(weather_data_float)
    except:
        return ()
    
    # Make a copy of the original list and reverse the order of the items on the list
    weather_data_reverse = weather_data_float.copy()
    weather_data_reverse.reverse()

    # Find the position of the minimum value in the reversed list
    min_position_reverse = weather_data_reverse.index(min_value)

    # To find the last position of the minimum value in the original list, minus the length of the list by 1 (to account for the index starting at 0) and minus the position of the minimum value in the reversed list
    min_position = (len(weather_data_float) - 1) - min_position_reverse

    return min_value, min_position

def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    weather_data_float = [float(value) for value in weather_data]
    
    try:
        max_value = max(weather_data_float)
    except:
        return ()
    
    # Make a copy of the original list and reverse the order of the items on the list
    weather_data_reverse = weather_data_float.copy()
    weather_data_reverse.reverse()

    # Find the position of the maximum value in the reversed list
    max_position_reverse = weather_data_reverse.index(max_value)

    # To find the last position of the maximum value in the original list, minus the length of the list by 1 (to account for the index starting at 0) and minus the position of the maximum value in the reversed list
    max_position = (len(weather_data_float) - 1) - max_position_reverse

    return max_value, max_position

def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    date_list = [row[0] for row in weather_data if row]
    min_temp_in_c_list = [convert_f_to_c(row[1]) for row in weather_data if row]
    max_temp_in_c_list = [convert_f_to_c(row[2]) for row in weather_data if row]

    number_of_days = len(date_list)
    min_temp, min_position = find_min(min_temp_in_c_list)
    max_temp, max_position = find_max(max_temp_in_c_list)
    date_of_min_temp = convert_date(date_list[min_position])
    date_of_max_temp = convert_date(date_list[max_position])
    mean_min_temp = round(calculate_mean(min_temp_in_c_list), 1)
    mean_max_temp = round(calculate_mean(max_temp_in_c_list), 1)

    summary_string = (
        f"{number_of_days} Day Overview\n"
        f"  The lowest temperature will be {format_temperature(min_temp)}, and will occur on {date_of_min_temp}.\n"
        f"  The highest temperature will be {format_temperature(max_temp)}, and will occur on {date_of_max_temp}.\n"
        f"  The average low this week is {format_temperature(mean_min_temp)}.\n"
        f"  The average high this week is {format_temperature(mean_max_temp)}.\n"
    )
    
    return summary_string

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    daily_summary_string = ""

    for row in weather_data:
        if row:
            formatted_date = convert_date(row[0])
            min_temp_in_c = convert_f_to_c(row[1])
            max_temp_in_c = convert_f_to_c(row[2])
            daily_summary_string += (
                f"---- {formatted_date} ----\n"
                f"  Minimum Temperature: {format_temperature(min_temp_in_c)}\n"
                f"  Maximum Temperature: {format_temperature(max_temp_in_c)}\n\n"
            )

    return daily_summary_string