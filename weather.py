import csv
from datetime import datetime

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
#-------------------DONE---------------------#


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    #give variable the ISO string, from/import datetime used to change it from a string
    date_data = datetime.fromisoformat(iso_string)

    #converting to a normal formatted date
    converted_date = date_data.strftime("%A %d %B %Y")

    return converted_date
#-------------------DONE---------------------#


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    #change to float value to match expected outcome
    f_temp = float(temp_in_farenheit)

    #convert f to c with maths and round up to 1 float decimal
    celcius_temp = round((f_temp - 32) * 5/9, 1)

    return celcius_temp
#-------------------DONE---------------------#


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    #change all temps in list to floats using list comprehension
    #for the nums (temps) in weather data, change to a float and add to this new list
    temp_nums = [float(nums) for nums in weather_data]

    #sum up
    total = round(sum(temp_nums), 5)

    #calculate mean/average - divide total by no. of temps in list
    mean = round(total / len(temp_nums), 5)

    return float(mean)
#-------------------DONE---------------------#


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    #open up test csv files and set name
    with open(csv_file, encoding="UTF-8") as my_file:

        #read the files but skip over the first line in each one
        reader = csv.reader(my_file, delimiter=',')
        next(reader)

    #list comprehension - make new list, add data in from CSV files, convert temps to integers
        rows = [[row[0], int(row[1]), int(row[2])] for row in reader if row]

    return rows
#-------------------DONE---------------------#


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list. 
        (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return ()

    #associate min temp with first list value
    min_temp = float(weather_data[0])
    mintemp_position = 0

    #search through list of temps to find min
    for weather in range(len(weather_data)):
        temps = float(weather_data[weather])

        if temps <= min_temp:
            min_temp = temps
            mintemp_position = weather

    return (min_temp, mintemp_position)
#-------------------DONE---------------------#


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
        (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return ()

    #associate max temp with first list value
    max_temp = float(weather_data[0])
    maxtemp_position = 0

    #search through list of temps to find max
    for weather in range(len(weather_data)):
        temps = float(weather_data[weather])

        if temps >= max_temp:
            max_temp = temps
            maxtemp_position = weather

    return (max_temp, maxtemp_position)
#-------------------DONE---------------------#



def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    weather_summary = ""

    # low_temps = [convert_f_to_c(min_temp) for iso_date, min_temp, max_temp in weather_data]
    # high_temps = [convert_f_to_c(max_temp) for iso_date, min_temp, max_temp in weather_data]

    #make blank lists to store test data
    low_temps = []
    high_temps = []

    #loop through info about each day from test data
    for iso_date, min_temp, max_temp in weather_data:

        #convert temps so long as they are ints/floats - use convert function from above
        if isinstance(min_temp, (int, float)) and isinstance(max_temp, (int, float)):
            low_temps.append(convert_f_to_c(min_temp))
            high_temps.append(convert_f_to_c(max_temp))

    #work out average low/high temps from each list
    avg_low = round(sum(low_temps) / len(low_temps), 1)
    avg_high = round(sum(high_temps) / len(high_temps), 1)
    
    #as lists not chronological, find position of min/max temps using min() and max()
    min_temp_position = min(low_temps)
    low_date = convert_date(weather_data[low_temps.index(min_temp_position)][0])

    max_temp_position = max(high_temps)
    high_date = convert_date(weather_data[high_temps.index(max_temp_position)][0])

    #count the rows in the test data to work out how many days summary is for
    overview_days = len(weather_data)

    weather_summary +=  (
                            f"{overview_days} Day Overview\n"
                            f"  The lowest temperature will be {min_temp_position}{DEGREE_SYBMOL}, and will occur on {low_date}.\n"
                            f"  The highest temperature will be {max_temp_position}{DEGREE_SYBMOL}, and will occur on {high_date}.\n"
                            f"  The average low this week is {avg_low}{DEGREE_SYBMOL}.\n"
                            f"  The average high this week is {avg_high}{DEGREE_SYBMOL}.\n"
                        )

    return weather_summary
#-------------------DONE?---------------------#



def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    weather_summary = ""

    for iso_date, min_temp, max_temp in weather_data:

        #make variable for date and convert using above function
        daily_sum_date = convert_date(iso_date)

        #convert f to c temps from data using above function
        min_convert = convert_f_to_c(min_temp)
        max_convert = convert_f_to_c(max_temp)

        weather_summary +=  (
                                f"---- {daily_sum_date} ----\n"
                                f"  Minimum Temperature: {min_convert}{DEGREE_SYBMOL}\n"
                                f"  Maximum Temperature: {max_convert}{DEGREE_SYBMOL}\n\n"
                            )

    return weather_summary
#-------------------DONE---------------------#