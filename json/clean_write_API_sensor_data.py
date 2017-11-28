import requests
import json

#GET https://api.connectsense.com/v1/{API_TOKEN}/devices/{DEVICE_SERIAL_NUMBER} for specific sensor
#GET https://api.connectsense.com/v1/{API_TOKEN}/devices for all sensors


API_TOKEN = "24DB3A5F73B12DC450FAF2718D78EB1B"
sensor_codes = {"ambient_temp": "49C2A9TH01", "drinks_fridge": "4852F6TH01", "food_fridge": "49C013TH01"}

# will hold the final json data to be written to file
sensors = []

def retrieve_sensor_data(sensor_code):
    '''
    takes everything from the API response and adds to list
    :param sensor_code: id code of the sensor
    :return: none
    '''
    request = requests.get('https://api.connectsense.com/v1/{}/devices/{}'.format(API_TOKEN, sensor_code))

    # Check for HTTP codes other than 200
    if request.status_code != 200:
        print('Status:', request.status_code, 'Problem with the request. Exiting.')
        exit()

    # transform API payload
    data = request.json()
    date, time = str(data['last_reported_at']).split('T')
    trimmed_time = time[0:8]
    sensor = {'serial_number': data['serial_number'],'name': data['name'],'date': date, 'time': trimmed_time, 'location': data['location'], 'temperature': data['temperature'], 'humidity': data['humidity']}
    # print(sensor)
    sensors.append(sensor)

def write_sensors_to_file():
    '''
    writes list of json sensors to file
    :return: none
    '''
    with open('sensor_data.json', 'a') as file:
        json.dump(sensors, file, indent=2)

def main():
    for sensor_code in sensor_codes.values():
        retrieve_sensor_data(sensor_code)
    write_sensors_to_file()

main()