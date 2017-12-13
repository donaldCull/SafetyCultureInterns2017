import sys
from connection_information import connect
import statistics
from datetime import timedelta
from generate_email_alert import send_email

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
        next_sensor_recording = latest_sensor_recording
        next_timestamp = latest_timestamp
        for index in range(len(sensor_temps)-1, -1, -1):
            if sensor_temps[index] >= sensor_temp_threshold:
                next_sensor_recording = sensor_temps[index]
                next_timestamp = sensor_timestamps[index]
            else:
                break
        time_diff = latest_timestamp - next_timestamp
        if time_diff > timedelta(hours=1):
            detection_template = "Anomaly detected in {} by {} ({}) at {} with a temperature of {} which started at {} with a temperature of {}. Temperature has been out of bounds for {}".format(sensor_serial_code['sensor_location'],
                                                                                                                sensor_serial_code['sensor_name'],
                                                                                                                sensor_serial_code['sensor_serial'],
                                                                                                                latest_timestamp, latest_sensor_recording,
                                                                                                                next_timestamp, next_sensor_recording, time_diff)
            print(detection_template)
            send_email(detection_template)
