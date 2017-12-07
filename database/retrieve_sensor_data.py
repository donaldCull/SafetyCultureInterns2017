import json
from datetime import datetime, timedelta

import requests

import sys;

sys.path.append('/Users/admin/PycharmProjects/SafetyCultureInterns2017/database/connection_information.py')

from connection_information import connect
from database.sensor_dict_collection import ListOfSensors

previous_time = {}
timezone_adjustment = 10

API_TOKEN = "24DB3A5F73B12DC450FAF2718D78EB1B"
sensors = ListOfSensors()

cursor = connect()

for sensor_code in sensors.values():
    previous_time_file = json.load(
        open("/Users/admin/PycharmProjects/SafetyCultureInterns2017/database/previous_time.json", "r"))
    # print(previous_time_file[sensor_code])
    previous_time[sensor_code] = previous_time_file[sensor_code]

print(previous_time)

# print("\nRunning Code - " + str(datetime.now()))

# run retrieval code
for sensor_code in sensors.values():
    request = requests.get('https://api.connectsense.com/v1/{}/devices/{}'.format(API_TOKEN, sensor_code))

    response, sensor_scrap = request.text.split(",\"recent_reportings")
    acceptable_string = response + "}"
    sensor_individual_details = json.loads(acceptable_string)

    # This is all just to makeup for timezone changes the API makes#
    temp_date_time = str(sensor_individual_details['last_reported_at']).replace("T", " ")[:-5]
    # print(temp_date_time)

    converted_date_time = datetime.strptime(temp_date_time, '%Y-%m-%d %H:%M:%S')

    time_adjusted = converted_date_time + timedelta(hours=timezone_adjustment)
    # print(converted_date_time)
    # print(time_adjusted)

    # Checking "previous_time" dictionary if time/date is the same, if not insert into database#
    if datetime.strftime(time_adjusted, "%Y-%m-%d %H:%M:%S") not in previous_time[sensor_code]:
        # sql execution
        sql_execution_individual_sensor_table = 'INSERT INTO ' + sensor_code + ' (sensor_date_time, ' \
                                                                               'sensor_temp, sensor_humid)' \
                                                                               ' VALUE ' \
                                                                               '("{}", "{}", "{}");' \
                                                                               ''.format(
            time_adjusted,
            sensor_individual_details['temperature'],
            sensor_individual_details['humidity'])
        print(sql_execution_individual_sensor_table)
        cursor.execute(sql_execution_individual_sensor_table)

        previous_time[sensor_code] = datetime.strftime(time_adjusted, "%Y-%m-%d %H:%M:%S")


    else:
        print("Most Recent API call for " + sensor_code + " existed within the database already.")

# update previous_time.json file
with open("/Users/admin/PycharmProjects/SafetyCultureInterns2017/database/previous_time.json", "w") as file:
    json.dump(previous_time, file)

print(previous_time)
