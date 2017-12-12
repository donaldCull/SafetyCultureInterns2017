import json

import requests

import utility_db_functions as udb

cursor = udb.connect()

user_id = 1

api_token = udb.get_api_token(user_id)

sensors = udb.ListOfAllSensors(api_token)
sql_partial = 'INSERT INTO Devices (sensor_serial, UserID, sensor_name, sensor_location) VALUE ("{}", "{}", "{}", "{}");'

for sensor_code in sensors.values():
    # print('https://api.connectsense.com/v1/{}/devices/{}'.format(API_TOKEN, sensor_code))
    request = requests.get('https://api.connectsense.com/v1/{}/devices/{}'.format(api_token, sensor_code), timeout=20)

    response, sensor_scrap = request.text.split(",\"recent_reportings")
    acceptable_string = response + "}"
    sensor_individual_details = json.loads(acceptable_string)
    # print(sensor_individual_details)

    sql_command = sql_partial.format(sensor_code, user_id, sensor_individual_details['name'],
                                     sensor_individual_details['location'])
    print(sql_command)
    cursor.execute(sql_command)
