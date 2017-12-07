sensor_date_time = []
import copy
import datetime

import pandas as pd

from database.connection_information import connect

cursor = connect()

sensors = {
    "ambient_temp": "49C2A9TH01", "drinks_fridge": "4852F6TH01", "food_fridge": "49C013TH01"}  # Generate Dynamically

sql_get_dates_incomplete = "SELECT * FROM {} WHERE sensor_date_time BETWEEN '{}' AND '{}';"

last_weeks_data = ""

todays_date = datetime.datetime.now().date()
seven_days_ago = todays_date - datetime.timedelta(days=7)
list_of_dates = pd.date_range(seven_days_ago, periods=7).tolist()
# print("Days: " + str(list_of_dates))
dict_of_temps = {}

dict_for_inserting = {}

for sensor_code in sensors.values():
    dict_of_temps[sensor_code] = []
    dict_for_inserting[sensor_code] = []

for sensor_code in sensors.values():
    sql_to_execute = sql_get_dates_incomplete.format(sensor_code, seven_days_ago, todays_date)
    # print(sql_to_execute)
    # list_of_values[sensor_code] = cursor.execute(sql_to_execute)
    cursor.execute(sql_to_execute)
    results = cursor.fetchall()
    dict_of_temps[sensor_code] = results
    # print(dict_of_values[sensor_code])

# Global variables - Overridden each loop
# sensor_date_time = []
sensor_temp = []

index_of_value = []
indexes_for_sensor = []

closest_time = []
list_of_times = []  # list of times from sensor for that day
new_list_of_times = []

# lists for each day
mon_temps = []
tue_temps = []
wed_temps = []
thu_temps = []
fri_temps = []
sat_temps = []
sun_temps = []

mon_times = []
tue_times = []
wed_times = []
thu_times = []
fri_times = []
sat_times = []
sun_times = []

list_closest_times = []

# Global Variables
times = [0, 6, 12, 18]  # Generate Dynamically

# Looping through every sensor in the "sensors" Dict
for sensor_code in sensors.values():
    print("\nFor sensor: " + sensor_code)
    # Separate dates, times and temps, maintaining order - from oldest to newest - in new lists
    # Reset/Clear sensor_dates = [], sensor_temps = [], closest_time = [],
    # index_of_value = [], indexes_for_sensor = [], list_of_times = []

    # reset lists for each day
    mon_temps.clear()
    tue_temps.clear()
    wed_temps.clear()
    thu_temps.clear()
    fri_temps.clear()
    sat_temps.clear()
    sun_temps.clear()

    for day in list_of_dates:
        # print("\n" + "Date: " + str(day.date()))

        sensor_date_time.clear()
        sensor_temp.clear()

        closest_time.clear()

        index_of_value.clear()
        indexes_for_sensor.clear()

        list_of_times.clear()
        new_list_of_times.clear()
        list_closest_times.clear()

        for data in dict_of_temps[sensor_code]:
            # print(data['sensor_date_time'].date(), day.date())
            if data['sensor_date_time'].date() == day.date():
                sensor_date_time.append(data['sensor_date_time'])
                sensor_temp.append(data['sensor_temp'])

        for my_times in times:
            # print("Get times for: " + str(my_times))
            # Gets closest time for each sensor
            # print(my_times)

            for sensor_dt in sensor_date_time:
                list_of_times.append(datetime.datetime.strftime(sensor_dt, "%H:%M:%S"))

            # print(type(datetime.timedelta(hours=my_times).seconds))
            # print(list_of_times)

            for line in list_of_times:
                # print("line" + line)
                new_line = datetime.datetime.strptime(line, "%H:%M:%S")
                new_line_2 = datetime.timedelta(hours=new_line.hour, minutes=new_line.minute, seconds=new_line.second)
                # print("newline" + str(new_line_2.total_seconds()))
                # print(type(new_line_2))

                new_list_of_times.append(new_line_2.total_seconds())
            # print(new_list_of_times)

            # print("List of times: " + str(new_list_of_times))
            # print("My time in seconds: " + str(datetime.timedelta(hours=my_times).seconds))

            try:
                nearest_time = min(new_list_of_times, key=lambda x: abs(x - datetime.timedelta(hours=my_times).seconds))
                closest_time.append(nearest_time)
            except ValueError:
                pass


                # print(closest_time)

        # print("Times (Values): " + str(closest_time))

        # Take each time value and get index of it from sensor_date_time and then get ref
        # print("Get indices of those values:")

        try:
            for x, y in enumerate(closest_time):
                list_closest_times.append(new_list_of_times.index(closest_time[int(x)]))

        except (ValueError, IndexError):
            pass

        try:
            if day.date().isoweekday() == 1:  # monday
                for o, i in enumerate(list_closest_times):
                    mon_temps.append(sensor_temp[list_closest_times[o]])

            if day.date().isoweekday() == 2:  # tuesday
                for o, i in enumerate(closest_time):
                    tue_temps.append(sensor_temp[list_closest_times[o]])

            if day.date().isoweekday() == 3:  # wednesday
                for o, i in enumerate(closest_time):
                    wed_temps.append(sensor_temp[list_closest_times[o]])

            if day.date().isoweekday() == 4:  # thursday
                for o, i in enumerate(closest_time):
                    thu_temps.append(sensor_temp[list_closest_times[o]])

            if day.date().isoweekday() == 5:  # friday
                for o, i in enumerate(closest_time):
                    fri_temps.append(sensor_temp[list_closest_times[o]])

            if day.date().isoweekday() == 6:  # saturday
                for o, i in enumerate(closest_time):
                    sat_temps.append(sensor_temp[list_closest_times[o]])

            if day.date().isoweekday() == 7:  # sunday
                for o, i in enumerate(closest_time):
                    sun_temps.append(sensor_temp[list_closest_times[o]])

        except (NameError, TypeError):
            pass

        dict_for_inserting[sensor_code] = {"Monday": copy.deepcopy(mon_temps), "Tuesday": copy.deepcopy(tue_temps),
                                           "Wednesday": copy.deepcopy(wed_temps), "Thursday": copy.deepcopy(thu_temps),
                                           "Friday": copy.deepcopy(fri_temps),
                                           "Saturday": copy.deepcopy(sat_temps), "Sunday": copy.deepcopy(sun_temps)}
        # print(dict_for_inserting)
        # print()

dict_for_inserting['Dates'] = [str(i.date()) for i in list_of_dates]
dict_for_inserting['Times'] = times

converted_dict = str(dict_for_inserting).replace("'", '"')

sql_for_inserting = "INSERT INTO Report(report_date, report_json) VALUE ('{}', '{}')".format(todays_date,
                                                                                             converted_dict)

print("\nSQL QUERY")
print(sql_for_inserting)
cursor.execute(sql_for_inserting)
