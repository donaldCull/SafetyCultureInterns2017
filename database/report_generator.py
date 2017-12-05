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
print("Days: " + str(list_of_dates))
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
sensor_date_time = []
sensor_temp = []

index_of_value = []
indexes_for_sensor = []

closest_time = []
list_of_times = []  # list of times from sensor for that day
new_list_of_times = []

# lists for each day
mon = []
tue = []
wed = []
thu = []
fri = []
sat = []
sun = []
inserting_times = []

# Global Variables
times = [0, 6, 12, 18]  # Generate Dynamically

# Looping through every sensor in the "sensors" Dict
for sensor_code in sensors.values():
    print("\nFor sensor: " + sensor_code)
    # Separate dates, times and temps, maintaining order - from oldest to newest - in new lists
    # Reset/Clear sensor_dates = [], sensor_temps = [], closest_time = [],
    # index_of_value = [], indexes_for_sensor = [], list_of_times = []

    # reset lists for each day
    mon.clear()
    tue.clear()
    wed.clear()
    thu.clear()
    fri.clear()
    sat.clear()
    sun.clear()
    inserting_times.clear()

    for day in list_of_dates:
        print("\n" + "Date/Time: " + str(day.date()))

        sensor_date_time.clear()
        sensor_temp.clear()

        closest_time.clear()

        index_of_value.clear()
        indexes_for_sensor.clear()

        list_of_times.clear()
        new_list_of_times.clear()

        for data in dict_of_temps[sensor_code]:
            # print(data['sensor_date_time'].date(), day.date())
            if data['sensor_date_time'].date() == day.date():
                sensor_date_time.append(data['sensor_date_time'])
                sensor_temp.append(data['sensor_temp'])

        for my_times in times:
            print("Get times for: " + str(my_times))
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

            closest_time.append(
                min(new_list_of_times, key=lambda x: abs(x - datetime.timedelta(hours=my_times).seconds)))
            # print(closest_time)

        print("Times (Values): " + str(closest_time))

        # Take each time value and get index of it from sensor_date_time and then get ref
        print("Get indices of those values:")

        test = new_list_of_times.index(closest_time[0])
        print(test)
        print(sensor_date_time[test], sensor_temp[test])
        test_2 = new_list_of_times.index(closest_time[1])
        print(test_2)
        print(sensor_date_time[test_2], sensor_temp[test_2])
        test_3 = new_list_of_times.index(closest_time[2])
        print(test_3)
        print(sensor_date_time[test_3], sensor_temp[test_3])
        test_4 = new_list_of_times.index(closest_time[3])
        print(test_4)
        print(sensor_date_time[test_4], sensor_temp[test_4])

        if day.date().isoweekday() == 1: #monday
            mon.append(sensor_temp[0])
            mon.append(sensor_temp[1])
            mon.append(sensor_temp[2])
            mon.append(sensor_temp[3])
        if day.date().isoweekday() == 2: #tuesday
            tue.append(sensor_temp[0])
            tue.append(sensor_temp[1])
            tue.append(sensor_temp[2])
            tue.append(sensor_temp[3])
        if day.date().isoweekday() == 3: #wednesday
            wed.append(sensor_temp[0])
            wed.append(sensor_temp[1])
            wed.append(sensor_temp[2])
            wed.append(sensor_temp[3])
        if day.date().isoweekday() == 4: #thursday
            thu.append(sensor_temp[0])
            thu.append(sensor_temp[1])
            thu.append(sensor_temp[2])
            thu.append(sensor_temp[3])
        if day.date().isoweekday() == 5: #friday
            fri.append(sensor_temp[0])
            fri.append(sensor_temp[1])
            fri.append(sensor_temp[2])
            fri.append(sensor_temp[3])
        if day.date().isoweekday() == 6: #saturday
            sat.append(sensor_temp[0])
            sat.append(sensor_temp[1])
            sat.append(sensor_temp[2])
            sat.append(sensor_temp[3])
        if day.date().isoweekday() == 7: #sunday
            sun.append(sensor_temp[0])
            sun.append(sensor_temp[1])
            sun.append(sensor_temp[2])
            sun.append(sensor_temp[3])


    # format stuff from above into dict
    # {_SENSOR_CODE_:{"Monday":[], "Tuesday":[], "Wednesday":[], "Thursday":[], "Friday":[], "Saturday":[], "Sunday":[]}

    dict_for_inserting[sensor_code] = {"Monday": mon, "Tuesday": tue, "Wednesday": wed, "Thursday": thu,
                                       "Friday": fri,
                                       "Saturday": sat, "Sunday": sun, "Times": inserting_times}

print("##")
print(dict_for_inserting)
