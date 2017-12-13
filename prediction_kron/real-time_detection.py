import sys
import os
import csv
from connection_information import connect
import statistics
from datetime import timedelta, datetime
from dateutil import parser
from generate_email_alert import send_email

last_time_reported = []
sys.path.append('sftp://ec2-52-207-83-62.compute-1.amazonaws.com/var/www/prediction')
cursor = connect()

get_user_sensors_sql = "SELECT sensor_serial, sensor_name, sensor_location FROM Devices;"
cursor.execute(get_user_sensors_sql)
sensor_serial_codes = cursor.fetchall()

for sensor_serial_code in sensor_serial_codes:
    get_sensor_data_sql = "SELECT sensor_date_time, sensor_temp FROM {};".format(sensor_serial_code['sensor_serial'])
    cursor.execute(get_sensor_data_sql)
    raw_sensor_data = cursor.fetchall()

    sensor_timestamps = []
    sensor_temps = []
    for row in raw_sensor_data:
        sensor_timestamps.append(row['sensor_date_time'])
        sensor_temps.append(float(row['sensor_temp']))

    temp_mean_sensor = statistics.mean(sensor_temps)
    temp_std_dev = statistics.stdev(sensor_temps)
    two_std_dev = temp_std_dev + temp_std_dev
    sensor_temp_threshold = temp_mean_sensor + temp_std_dev
    print("Sensor {} has threshold {}".format(sensor_serial_code['sensor_serial'], sensor_temp_threshold))

    latest_sensor_recording = sensor_temps[-1]
    latest_sensor_recording_index = sensor_temps.index(sensor_temps[-1])
    latest_timestamp = sensor_timestamps[-1]

    if latest_sensor_recording >= sensor_temp_threshold:
        # initialise values in case the next value is under the threshold
        next_sensor_recording = latest_sensor_recording
        next_timestamp = latest_timestamp
        # Go backwards from the latest observation and check how long the anomaly has lasted
        for index in range(len(sensor_temps)-1, -1, -1):
            if sensor_temps[index] >= sensor_temp_threshold:
                next_sensor_recording = sensor_temps[index]
                next_timestamp = sensor_timestamps[index]
            else:
                break


        time_diff = latest_timestamp - next_timestamp
        # open reported sensors and check if the sensor has already been reported on lately
        reported_sensors = {}
        with open('reported_sensors.csv') as file:
            reader = csv.reader(file)
            for row in reader:
                reported_sensors[row[0]] = parser.parse(row[1])
        # if the anomaly has lasted for more than 1 hour and an email hasnt been sent in the last hour
        if time_diff > timedelta(hours=1) and reported_sensors[sensor_serial_code['sensor_serial']] > datetime.now() - timedelta(hours=1):
            detection_template = "Anomaly detected in {} by {} ({}) at {} with a temperature of {} which started at {} with a temperature of {}. Temperature has been out of bounds for {}".format(sensor_serial_code['sensor_location'],
                                                                                                                sensor_serial_code['sensor_name'],sensor_serial_code['sensor_serial'],
                                                                                                                latest_timestamp, latest_sensor_recording,next_timestamp, next_sensor_recording, time_diff)
            print(detection_template)
            send_email(detection_template)
            last_time_reported.append([sensor_serial_code['sensor_serial'], latest_timestamp])
# check if there were any anomalies reported and write them to the csv to be checked next time
if len(last_time_reported) != 0:
    with open(os.path.dirname(__file__) + '/reported_sensors.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerows(last_time_reported)

