import csv
from datetime import datetime, time
import statistics
import itertools
from unittest import result

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
        
    """Converts an ISO formatted date into a human readable format. 

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    convert_date = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return convert_date.strftime("%A %d %B %Y")

def convert_f_to_c(temp_in_farenheit):

    """Converts an temperature from farenheit to celcius.

     Args:
         temp_in_farenheit: float representing a temperature.
     Returns:
         A float representing a temperature in degrees celcius, rounded to 1dp.
     """

    
    temp_in_celsius = (float(temp_in_farenheit) - 32) * (5/9)
    result = round(temp_in_celsius, 1)

    return result

def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.
    @@ -45,6 +39,17 @@ def calculate_mean(weather_data):
         weather_data: a list of numbers.
     Returns:
         A float representing the mean value."""

    sum = 0
    length = len(weather_data)

    for weather in weather_data:
        sum += float(weather)
    mean_of_list = sum / length
    return(mean_of_list)

def load_data_from_csv(csv_file):

    """  csv_file: a string representing the file path to a csv file.
     Returns:
         A list of lists, where each sublist is a (non-empty) line in the csv file.

    """
    import csv

    weather_data = []
   
    with open(csv_file, encoding="utf-8") as csv_file: 
        reader = csv.reader(csv_file, delimiter = ",")
        next(reader)
        for line in reader: 
            if line:
                weather_data.append([line[0],float(line[1]),float((line[2]))])      
        return weather_data
 
def find_min(weather_data):

    """Calculates the minimum value in a list of numbers.
    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """

    if len(weather_data) == 0:
        return ()
    else:
        min_value = float(weather_data[0])
        min_index = 0
        for index in range(len(weather_data)):
            if float(weather_data[index]) <= min_value:
                min_value = float(weather_data[index])
                min_index = index
        return min_value, min_index

def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.
    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    if len(weather_data) == 0:
        return ()
    else:
        max_value = float(weather_data[0])
        max_index = 0
        for index in range(len(weather_data)):
            if float(weather_data[index]) >= max_value:
                max_value = float(weather_data[index])
                max_index = index
        return max_value, max_index

def generate_summary(weather_data):
    """Outputs a summary for the given weather data.
    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    length = len(weather_data)
    min_temp = [minimum[1] for minimum in weather_data]
    max_temp = [maximum[2] for maximum in weather_data]
    date = [day[0] for day in weather_data]

    min_in_weather_data = find_min(min_temp)
    min_c__weather_summary = convert_f_to_c(min_in_weather_data[0])
    index_of_min_day = min_in_weather_data[1]
    min_day_in_weather_data =  convert_date(date[index_of_min_day])

    max_in_weather_data = find_max(max_temp)
    max_c__weather_summary = convert_f_to_c(max_in_weather_data[0])
    index_of_max_day = max_in_weather_data[1]
    max_day_in_weather_data =  convert_date(date[index_of_max_day])

    average_min_temp_f = calculate_mean(min_temp)
    average_max_temp_f = calculate_mean(max_temp)

    average_min_temp_c = convert_f_to_c(average_min_temp_f)
    average_max_temp_c = convert_f_to_c(average_max_temp_f)

    day = f"{length} Day Overview"
    lowest_temp_ouput = f"  The lowest temperature will be {min_c__weather_summary}°C, and will occur on {min_day_in_weather_data}."
    highest_temp_output = f"  The highest temperature will be {max_c__weather_summary}°C, and will occur on {max_day_in_weather_data}."
    average_low_ouput = f"  The average low this week is {average_min_temp_c}°C."
    average_high_output = f"  The average high this week is {average_max_temp_c}°C."

    summary = "{0}\n{1}\n{2}\n{3}\n{4}\n".format(day, lowest_temp_ouput, highest_temp_output, average_low_ouput, average_high_output)

    return summary
#   8 Day Overview
#     The lowest temperature will be 8.3°C, and will occur on Friday 19 June 2020.
#     The highest temperature will be 22.2°C, and will occur on Sunday 21 June 2020.
#     The average low this week is 11.4°C.
#     The average high this week is 18.8°C.
 
def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.
    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    daily_summary_list = []
    final_day = []
    final_min = []
    final_max = []
    summary = ""

    for data in weather_data:
        iso_day = data[0]
        min_temp = data[1]
        max_temp = data[2]
        
        converted_day = convert_date(iso_day)
        convert_min_to_c = convert_f_to_c(min_temp)
        convert_max_to_c = convert_f_to_c(max_temp)
                
        daily_summary_list.append(converted_day) 
        daily_summary_list.append(convert_min_to_c) 
        daily_summary_list.append(convert_max_to_c) 
   
    summary_data = [data for data in daily_summary_list]
    day = summary_data[0::3]
    minimum = summary_data[1::3]
    maximum = summary_data[2::3]
   
    i = 0
    while i < len(day):
        day_output = f"---- {day[i]} ----"
        i += 1
        final_day.append(day_output)       

    j = 0
    while j < len(minimum):
        min_output = f"  Minimum Temperature: {minimum[j]}°C"
        j += 1
        final_min.append(min_output)

    k = 0
    while k < len(maximum):
        max_output = f"  Maximum Temperature: {maximum[k]}°C"
        k += 1
        final_max.append(max_output)   
    
    for (a, b, c) in zip(final_day, final_min, final_max):
        final_data = "{0}\n{1}\n{2}\n\n".format(a, b, c)
        summary += final_data
        
    return summary       