import json

import requests

from connection_information import connect
from sensor_dict_collection import ListOfSensors

cursor = connect()

API_TOKEN = "24DB3A5F73B12DC450FAF2718D78EB1B"
sensors = ListOfSensors()
sql_partial = 'INSERT INTO ' + '{} (sens_name, sens_serial, sens_location) VALUE ("{}", "{}", "{}");'

for sensor_code in sensors.values():
    # print('https://api.connectsense.com/v1/{}/devices/{}'.format(API_TOKEN, sensor_code))
    request = requests.get('https://api.connectsense.com/v1/{}/devices/{}'.format(API_TOKEN, sensor_code), timeout=20)

    response, sensor_scrap = request.text.split(",\"recent_reportings")
    acceptable_string = response + "}"
    sensor_individual_details = json.loads(acceptable_string)
    # print(sensor_individual_details)

    sql_command = sql_partial.format("DevicesList", sensor_individual_details['name'], sensor_code,
                                     sensor_individual_details['location'])
    print(sql_command)
    cursor.execute(sql_command)
