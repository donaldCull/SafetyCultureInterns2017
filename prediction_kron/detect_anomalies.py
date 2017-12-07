import csv
import statistics
from dateutil import parser

sensor_filenames = []
sensor_names = []

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
with open('sensor_forecast_filenames.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        forecast_filenames.append(str(row).lstrip('[').rstrip(']').strip("'"))

threshold_counter = 0
for index, forecast_filename in enumerate(forecast_filenames):
    with open(forecast_filename) as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            row[0] = parser.parse(row[0])
            row[1] = float(row[1])
            forecasts.append(row)
        for temp in forecasts:
            if temp[1] >= thresholds[threshold_counter]:
                print("Anomaly Predicted with {} on {} at {} with a temperature of {}".format(sensor_names[index],row[0].date(), row[0].time(),
                                                                                    row[1]))
    forecasts.clear()
    threshold_counter += 1

