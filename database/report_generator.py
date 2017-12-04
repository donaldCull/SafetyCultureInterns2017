import datetime

import pandas as pd

from database.connection_information import connect

cursor = connect()

sensors = {
    "ambient_temp": "49C2A9TH01"}  # , "drinks_fridge": "4852F6TH01", "food_fridge": "49C013TH01"} # Generate Dynamically

sql_get_dates_incomplete = "SELECT * FROM {} WHERE sensor_date_time BETWEEN '{}' AND '{}';"

last_weeks_data = ""

todays_date = datetime.datetime.now().date()
seven_days_ago = todays_date - datetime.timedelta(days=7)
list_of_dates = pd.date_range(seven_days_ago, periods=7).tolist()

print(list_of_dates)

dict_of_values = {}

for sensor_code in sensors.values():
    dict_of_values[sensor_code] = []

for sensor_code in sensors.values():
    sql_to_execute = sql_get_dates_incomplete.format(sensor_code, seven_days_ago, todays_date)
    # print(sql_to_execute)
    # list_of_values[sensor_code] = cursor.execute(sql_to_execute)
    cursor.execute(sql_to_execute)
    results = cursor.fetchall()
    dict_of_values[sensor_code] = results
    # print(dict_of_values[sensor_code])

# TODO: Rewrite code to get this data (scalable) from the sensors and generate the JSON string to be input into the database.
# {_SENSOR_CODE_:{"Monday":[], "Tuesday":[], "Wednesday":[], "Thursday":[], "Friday":[], "Saturday":[], "Sunday":[]}

# Global variables - Overridden each loop
sensor_dates_times = []
sensor_temps = []

closest_time = []

index_of_value = []
indexes_for_sensor = []

list_of_times = []

that_days_sensor_data = [] #list of times from sensor for that day

# Global Variables
times = [0, 6, 12, 18]  # Generate Dynamically

# Looping through every sensor in the "sensors" Dict
for sensor_code in sensors.values():
    # Separate dates, times and temps, maintaining order - from oldest to newest - in new lists
    # Reset/Clear sensor_dates = [], sensor_temps = [], closest_time = [],
    # index_of_value = [], indexes_for_sensor = [], list_of_times = []

    for day in list_of_dates:
        print("\n" + str(day))

        sensor_dates_times.clear()
        sensor_temps.clear()

        closest_time.clear()

        index_of_value.clear()
        indexes_for_sensor.clear()

        list_of_times.clear()

        that_days_sensor_data.clear()

        for data in dict_of_values[sensor_code]:
            if data in day.to_pydatetime:
                sensor_dates_times.append(data['sensor_date_time'])
                sensor_temps.append(data['sensor_temp'])

        print(sensor_dates_times, sensor_temps)

        for my_times in times:
            # Gets closest time for each sensor
            # print(my_times)


            for sensor_dt in sensor_dates_times:
                that_days_sensor_data = datetime.datetime.strftime(sensor_dt, "%H:%M:%S")

            # print(list_of_times)
            closest_time.append(min(list_of_times, key=lambda x: abs(x - datetime.timedelta(hours=my_times))))

        print("Times: " + str(closest_time))

        # Take each time and get index of it from sensor_time and then get ref
        for c_time in closest_time:
            index_of_value.append(sensor_dates_times.index(c_time))

        print("Indexes: " + str(index_of_value))

        #












#######################################################################################################################

# print(list_of_values['49C2A9TH01'][0]['sensor_time'])
# variable = dict_of_values['49C2A9TH01'][0]['sensor_time']
# print(variable == dict_of_values['49C2A9TH01'][0]['sensor_time'])



# # todo gets all of the dates, times and temps of the first sensor to search through
# sensor_1_dates = []
# sensor_1_times = []
# sensor_1_temps = []
# for sensor_date in dict_of_values['49C2A9TH01']:
#     sensor_1_dates.append(sensor_date['sensor_date'])
#     sensor_1_times.append(sensor_date['sensor_time'])
#     sensor_1_temps.append(sensor_date['sens_temp'])
#
# sensor_2_dates = []
# sensor_2_times = []
# sensor_2_temps = []
# for sensor_date in dict_of_values['4852F6TH01']:
#     sensor_2_dates.append(sensor_date['sensor_date'])
#     sensor_2_times.append(sensor_date['sensor_time'])
#     sensor_2_temps.append(sensor_date['sens_temp'])
#
# sensor_3_dates = []
# sensor_3_times = []
# sensor_3_temps = []
# for sensor_date in dict_of_values['49C013TH01']:
#     sensor_3_dates.append(sensor_date['sensor_date'])
#     sensor_3_times.append(sensor_date['sensor_time'])
#     sensor_3_temps.append(sensor_date['sens_temp'])
#
# # print(sensor_1_times)
#
# # todo selected time intervals
# times = [4, 8, 12, 16, 20, 24]
#
#
#
#
# # print(times[0])
# # closest_time = min(sensor_1_times, key=lambda x:abs(x-datetime.timedelta(hours=10)))
# # print('Expecting 10:01:01')
# # for sensor_time in sensor_1_times:
#     # print(sensor_time)
#
#
#
# # todo find times in the first sensor that are closest to these time intervals
# sensor1_closest_times = []
# sensor2_closest_times = []
# sensor3_closest_times = []
# for time in times:
#     sensor1_closest_times.append(min(sensor_1_times, key=lambda x: abs(x - datetime.timedelta(hours=time))))
#     sensor2_closest_times.append(min(sensor_2_times, key=lambda x: abs(x - datetime.timedelta(hours=time))))
#     sensor3_closest_times.append(min(sensor_3_times, key=lambda x: abs(x - datetime.timedelta(hours=time))))
#
#
# # print(sensor2_closest_times)
# # print(sensor3_closest_times)
#
#     # print(closest_times)
# # print(closest_times[-1])
# # selected_index = sensor_1_times.index(closest_times[-1])
#
#
#
# # todo find the index of the these closest times in the data and retrieve date and temp
# for closest_time in sensor1_closest_times:
#     selected_index = sensor_1_times.index(closest_time)
#     #print("Selected time: {} {} {}".format(sensor_1_dates[selected_index], sensor_1_times[selected_index], sensor_1_temps[selected_index]) )
#
# print()
# for closest_time in sensor2_closest_times:
#     selected_index = sensor_2_times.index(closest_time)
#     #print("Selected time: {} {} {}".format(sensor_2_dates[selected_index], sensor_2_times[selected_index], sensor_2_temps[selected_index]) )
#
# print()
#
# for closest_time in sensor3_closest_times:
#     selected_index = sensor_3_times.index(closest_time)
#     #print("Selected time: {} {} {}".format(sensor_3_dates[selected_index], sensor_3_times[selected_index], sensor_3_temps[selected_index]) )
#
# # print(closest_time)
#
# # print(list( list_of_values.keys()) [list(list_of_values.values()).index(closest_time)])
# # time_in_seconds = datetime.timedelta.total_seconds(closest_time)
# # print(time_in_seconds)
# # print(list(dict_of_values.keys())[list(dict_of_values.values()).index(str(time_in_seconds))])
# # print(variable)
# print(list(dict_of_values.keys())[list(dict_of_values['49C2A9TH01'][0].values()).index(closest_time)])
# print(datetime.timedelta.total_seconds(closest_time))
# for sensor_code in sensors.values():
#     for sensor_date in dict_of_values[sensor_code]:
#         print(sensor_date['sensor_time'] == closest_time)

# print(list(dict_of_values['4852F6TH01'].values()))
# print(list_of_values.keys())
