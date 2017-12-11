# Set to run on the Crontab every minute.
# Gets the most recent data from each sensor.
# TODO: Get data from each sensor from each user.

import json
import os
import sys
from datetime import datetime, timedelta

import requests

import retrieve_user_info
from connection_information import connect
from sensor_dictionaries import ListOfAllSensors

# Local path, will have to be changed for the cron directory
sys.path.append('sftp://ec2-user@ec2-52-90-110-172.compute-1.amazonaws.com/var/www/data')

previous_time = {}
timezone_adjustment = 10

API_TOKEN = retrieve_user_info.get_api_token("1")
sensors = ListOfAllSensors(API_TOKEN)

cursor = connect()

for sensor_code in sensors.values():
    previous_time_file = json.load(
        open(os.path.dirname(__file__) + "/previous_time.json", "r"))
    # print(previous_time_file[sensor_code])
    previous_time[sensor_code] = previous_time_file[sensor_code]

print(previous_time)

# Loop for each sensor in "sensors" dictionary
for sensor_code in sensors.values():
    request = requests.get('https://api.connectsense.com/v1/{}/devices/{}'.format(API_TOKEN, sensor_code), timeout=20)

    response, sensor_scrap = request.text.split(",\"recent_reportings")
    acceptable_string = response + "}"
    sensor_individual_details = json.loads(acceptable_string)

    # This is all just to makeup for timezone changes the API makes#
    temp_date_time = str(sensor_individual_details['last_reported_at']).replace("T", " ")[:-5]
    # print(temp_date_time)

    converted_date_time = datetime.strptime(temp_date_time, '%Y-%m-%d %H:%M:%S')

    time_adjusted = converted_date_time + timedelta(hours=timezone_adjustment)

    # Check "previous_time" dictionary if time/date is the same, if not, then insert into database#
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

# Update previous_time.json file with most recent datetime
with open(os.path.dirname(__file__) + "/previous_time.json", "w") as file:
    json.dump(previous_time, file)

print(previous_time)
