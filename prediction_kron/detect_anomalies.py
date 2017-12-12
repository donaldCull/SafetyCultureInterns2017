import csv
import os
import statistics
import sys

from dateutil import parser
from connect_to_db import connect

sys.path.append('sftp://ec2-52-207-83-62.compute-1.amazonaws.com/var/www/prediction')

def detect():
    sensor_filenames = []
    sensor_names = []
    sensors = {}
    with open(os.path.dirname(__file__) + '/sensor_details.txt') as file:
        sensor_details = file.readlines()
        for line in sensor_details:
            code, name, location = line.strip().split(',')
            sensors[code] = name, location
    with open(os.path.dirname(__file__) + '/sensor_filenames.csv') as file:

        reader = csv.reader(file)
        for row in reader:
            sensor_filenames.append(str(row).lstrip('[').rstrip(']').strip("'"))
    for sensor_filename in sensor_filenames:
        sensor_name, file_type_scrap = str(sensor_filename).split('.')
        sensor_names.append(sensor_name)
    sensor_means = []
    sensor_temps = []
    thresholds = []
    two_std_devs = []
    std_devs = []
    # retrieve sensor temps from each sensor
    for sensor_filename in sensor_filenames:
        with open(os.path.dirname(__file__) + "/" + sensor_filename) as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                sensor_temps.append(float(row[1]))
        sensor_mean = statistics.mean(sensor_temps)
        sensor_means.append(sensor_mean)
        std_dev = statistics.stdev(sensor_temps)
        std_devs.append(std_dev)
        # determine the threshold for each sensor
        two_std_dev = std_dev + std_dev
        two_std_devs.append(two_std_dev)
        threshold = sensor_mean + two_std_dev
        thresholds.append(round(threshold, 2))
        sensor_temps.clear()
    for index, sensor_result in enumerate(range(len(sensor_means))):
        print("Sensor {}: mean {}, std. {}, 2std. {}, threshold {}".format(sensor_names[index],
                                                                           sensor_means[sensor_result],
                                                                           std_devs[sensor_result],
                                                                           two_std_devs[sensor_result],
                                                                           thresholds[sensor_result]))

    # search the sensor predictions to determine if there is a breach
    forecast_filenames = []
    forecasts = []
    incomplete_incident_sql = 'INSERT INTO Incidents (incid_serial, incid_location, incid_name, incid_date_start, incid_time_start, incid_temp) VALUE ("{}", "{}", "{}","{}", "{}", "{}");'
    with open(os.path.dirname(__file__) + '/sensor_forecast_filenames.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            forecast_filenames.append(str(row).lstrip('[').rstrip(']').strip("'"))

    for index, forecast_filename in enumerate(forecast_filenames):
        with open(os.path.dirname(__file__) + "/" + forecast_filename) as file:

            reader = csv.reader(file)
            next(reader)
            for row in reader:
                row[0] = parser.parse(row[0])
                row[1] = float(row[1])
                forecasts.append(row)

            for temp in forecasts:

                if temp[1] >= thresholds[index]:
                    detected_sensor = sensor_names[index]
                    start_detection_date = temp[0].date()
                    start_detection_time = temp[0].time()
                    detected_temp = temp[1]
                    detected_sensor_name = sensors[detected_sensor][0]
                    detected_sensor_location = sensors[detected_sensor][1]
                    anomaly_email_template = "Anomaly Predicted with {} sensor ({}) located at {} on {} at {} with a temperature of {} and will be resolved at ".format(
                        detected_sensor_name, detected_sensor, detected_sensor_location, start_detection_date,
                        start_detection_time, detected_temp)
                    cursor = connect()
                    complete_incident_sql = incomplete_incident_sql.format(detected_sensor, detected_sensor_location,
                                                                           detected_sensor_name, start_detection_date,
                                                                           start_detection_time, detected_temp)
                    cursor.execute(complete_incident_sql)

        forecasts.clear()

if __name__ == '__main__':
    detect()
