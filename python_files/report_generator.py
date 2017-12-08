import copy
import datetime

import pandas as pd

from connection_information import connect
from sensor_dict_collection import ListOfSensors

# Lists that are used, are cleared frequently
sensor_temp = []

index_of_value = []
indexes_for_sensor = []
sensor_date_time = []

closest_time = []
list_of_times = []  # list of times from sensor for that day
new_list_of_times = []

# TODO: One list for temp and times?
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

last_weeks_data = ""
dict_of_temps = {}
dict_for_inserting = {}

interval_times = [0, 6, 12, 18]  # TODO: Generate Dynamically

sql_get_dates_incomplete = "SELECT * FROM {} WHERE sensor_date_time BETWEEN '{}' AND '{}';"

cursor = connect()

sensors = ListOfSensors()

# Initialising dates
todays_date = datetime.datetime.now().date()  # Date when script is run
seven_days_ago = todays_date - datetime.timedelta(days=7)  # Date 7 days ago from when script is ru
list_of_dates = pd.date_range(seven_days_ago, periods=7).tolist()  # A list of these dates

# Initialising based stuff that has all the sensors
for sensor_code in sensors.values():
    dict_of_temps[sensor_code] = []
    dict_for_inserting[sensor_code] = []
    sql_to_execute = sql_get_dates_incomplete.format(sensor_code, seven_days_ago, todays_date)
    cursor.execute(sql_to_execute)
    results = cursor.fetchall()
    dict_of_temps[sensor_code] = results

# Looping through every sensor in the "sensors" Dict
for sensor_code in sensors.values():
    print("\nFor sensor: " + sensor_code)

    # Clear lists for each day
    mon_temps.clear()
    tue_temps.clear()
    wed_temps.clear()
    thu_temps.clear()
    fri_temps.clear()
    sat_temps.clear()
    sun_temps.clear()

    for day in list_of_dates:
        print("\n" + "Date: " + str(day.date()))

        # Clearing more lists that will be looped through again
        closest_time.clear()
        index_of_value.clear()
        indexes_for_sensor.clear()
        list_of_times.clear()
        list_closest_times.clear()
        new_list_of_times.clear()
        sensor_date_time.clear()
        sensor_temp.clear()

        for data in dict_of_temps[sensor_code]:
            # print(data['sensor_date_time'].date(), day.date())
            if data['sensor_date_time'].date() == day.date():
                sensor_date_time.append(data['sensor_date_time'])
                sensor_temp.append(data['sensor_temp'])

        for my_times in interval_times:
            for sensor_dt in sensor_date_time:
                list_of_times.append(datetime.datetime.strftime(sensor_dt, "%H:%M:%S"))

            for line in list_of_times:
                new_line = datetime.datetime.strptime(line, "%H:%M:%S")
                new_line_2 = datetime.timedelta(hours=new_line.hour, minutes=new_line.minute, seconds=new_line.second)

                new_list_of_times.append(new_line_2.total_seconds())

            try:
                nearest_time = min(new_list_of_times, key=lambda x: abs(x - datetime.timedelta(hours=my_times).seconds))
                closest_time.append(nearest_time)
            except ValueError:
                pass

        # Prints closest time (in deltatime.seconds) to the intervals in "interval_times"
        print("Times (intervals: " + str(interval_times))
        print("Times (seconds):  " + str(closest_time))

        try:
            for x, y in enumerate(closest_time):
                list_closest_times.append(new_list_of_times.index(closest_time[int(x)]))

        except (ValueError, IndexError):
            pass

        # TODO: Put this in another loop somehow, can see issue because each day has its own list of temps
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

    # Prints dict as it's completed for each sensor
    # print(dict_for_inserting)

# Add dates and times to end of dictionary
dict_for_inserting['Dates'] = [str(i.date()) for i in list_of_dates]
dict_for_inserting['Times'] = interval_times

converted_dict = str(dict_for_inserting).replace("'", '"')

sql_insert_report_incomplete = "INSERT INTO Report(report_date, report_json) VALUE ('{}', '{}')".format(todays_date,
                                                                                                        converted_dict)

print("\nSQL QUERY")
print(sql_insert_report_incomplete)
cursor.execute(sql_insert_report_incomplete)
