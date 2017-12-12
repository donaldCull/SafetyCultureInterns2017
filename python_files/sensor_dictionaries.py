# Call this file to generate a dictionary of all sensors with temperature's and humidity's attached to them
# Returns dict of sensors: {"[SENSOR NAME]": "[SENSOR CODE]", "[SENSOR NAME]": "[SENSOR CODE]"}

import json

import requests

from connection_information import connect

cursor = connect()


# Returns all sensors from API for user specified (by passing in their api_token)
def ListOfAllSensors(api_token):
    sensor = {}
    api_url = 'https://api.connectsense.com/v1/{}/devices/'.format(api_token)
    request = requests.get(api_url, timeout=20)

    dictionary_from_requests = json.loads(request.text)

    # print(dictionary_from_requests)

    for i, e in enumerate(dictionary_from_requests):
        if 'temperature' in e:
            # print(dictionary_from_requests[i]['name'])
            # print(dictionary_from_requests[i]['serial_number'])
            sensor[dictionary_from_requests[i]['name']] = dictionary_from_requests[i]['serial_number']

    # print(sensor)
    return sensor


# Used for generating reports
def ListOfUserSensors(user_id):
    sql_query_users_devices = "SELECT sensor_serial, sensor_name FROM Devices WHERE UserID = {}".format(user_id)
    cursor.execute(sql_query_users_devices)
    sensors = cursor.fetchall()
    return_sensor = {}

    for sensor in sensors:
        return_sensor[sensor['sensor_name']] = sensor['sensor_serial']

    print(return_sensor)
    return return_sensor
