# Call this file to generate a dictionary of all sensors with temperature's and humidity's attached to them
# Returns dict of sensors: {"[SENSOR NAME]": "[SENSOR CODE]", "[SENSOR NAME]": "[SENSOR CODE]"}

import json

import requests

from python_files.connection_information import connect

API_TOKEN = "24DB3A5F73B12DC450FAF2718D78EB1B"
API_URL = 'https://api.connectsense.com/v1/{}/devices/'.format(API_TOKEN)

sensor = {}


def ListOfSensors():
    cursor = connect()

    request = requests.get(API_URL, timeout=20)

    dictionary_from_requests = json.loads(request.text)

    # print(dictionary_from_requests)

    for i, e in enumerate(dictionary_from_requests):
        if 'temperature' in e:
            # print(dictionary_from_requests[i]['name'])
            # print(dictionary_from_requests[i]['serial_number'])
            sensor[dictionary_from_requests[i]['name']] = dictionary_from_requests[i]['serial_number']

    # print(sensor)
    return sensor
