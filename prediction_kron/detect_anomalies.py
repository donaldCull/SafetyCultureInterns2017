import csv
import statistics
from dateutil import parser

sensor_filenames = []
sensor_names = []
sensors = {}

with open('sensor_details.txt') as file:
    sensor_details = file.readlines()
    for line in sensor_details:
        code, name, location = line.strip().split(',')
        sensors[code] = name, location


with open('sensor_filenames.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        # forecast_filenames.append(row)
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
    with open(sensor_filename) as file:
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
    thresholds.append(threshold)
    sensor_temps.clear()

for index, sensor_result in enumerate(range(len(sensor_means))):
    print("Sensor {}: mean {}, std. {}, 2std. {}, threshold {}".format(sensor_names[index], sensor_means[sensor_result], std_devs[sensor_result], two_std_devs[sensor_result], thresholds[sensor_result]))


# search the sensor predictions to determine if there is a breach
forecast_filenames = []
forecasts = []
anomaly_detected = False
anomaly_email_template = ""
incidents_to_insert = []
incident = []

with open('sensor_forecast_filenames.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        forecast_filenames.append(str(row).lstrip('[').rstrip(']').strip("'"))

for index, forecast_filename in enumerate(forecast_filenames):
    with open(forecast_filename) as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            row[0] = parser.parse(row[0])
            row[1] = float(row[1])
            forecasts.append(row)

        for temp in forecasts:

            if anomaly_detected and temp[1] < thresholds[index]:
                end_detection_date = temp[0].date()
                end_detection_time = temp[0].time()
                incident.append(end_detection_date)
                incident.append(end_detection_time)
                anomaly_email_template += str(temp[0])
                anomaly_detected = False
                print(anomaly_email_template)
                incidents_to_insert.append(str(incident)+'\n')
                incident.clear()


            if temp[1] >= thresholds[index]:
                detected_sensor = sensor_names[index]
                start_detection_date = temp[0].date()
                start_detection_time = temp[0].time()
                detected_temp = temp[1]
                detected_sensor_name = sensors[detected_sensor][0]
                detected_sensor_location = sensors[detected_sensor][1]
                anomaly_email_template = "Anomaly Predicted with {} sensor ({}) located at {} on {} at {} with a temperature of {} and will be resolved at ".format(detected_sensor_name, detected_sensor, detected_sensor_location, start_detection_date, start_detection_time, detected_temp)
                # pID, incid_serial, incid_location, incid_name, incid_date_start, incid_time_start, incid_temp, incid_date_stop, incid_time_stop
                incident.append(detected_sensor)
                incident.append(detected_sensor_location)
                incident.append(detected_sensor_name)
                incident.append(start_detection_date)
                incident.append(start_detection_time)
                incident.append(detected_temp)
                anomaly_detected = True

    forecasts.clear()

with open('incidents_to_be_inserted.txt', 'w') as file:
    file.writelines(incidents_to_insert)