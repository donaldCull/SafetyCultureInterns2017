import requests
import json

# GET https://api.connectsense.com/v1/{API_TOKEN}/devices/{DEVICE_SERIAL_NUMBER} for specific sensor
# GET https://api.connectsense.com/v1/{API_TOKEN}/devices for all sensors

API_TOKEN = "24DB3A5F73B12DC450FAF2718D78EB1B"
sensors = {"ambient_temp": "49C2A9TH01", "drinks_fridge": "4852F6TH01", "food_fridge": "49C013TH01"}

def retrieve_sensor_data(sensor_code):
    """

    :param sensor_code: id code of the sensor
    :return: dictionary of useful details
    """

    request = requests.get('https://api.connectsense.com/v1/{}/devices/{}'.format(API_TOKEN, sensor_code))
    # remove unnecessary sensor information
    response, sensor_scrap = request.text.split(",\"recent_reportings")

    # add curly brace at the end of the string
    acceptable_string = response + "}"

    # turn literal string into a dictionary
    sensor_details = json.loads(acceptable_string)
    return sensor_details


def fetch():
    sensor_details = []
    for sensor_code in sensors.values():
        sensor_details.append(retrieve_sensor_data(sensor_code))
    return sensor_details
