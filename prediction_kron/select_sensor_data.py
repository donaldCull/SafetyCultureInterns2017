import csv

import os
import pandas as pd
import sys
from fbprophet import Prophet
from datetime import datetime, timedelta
from connection_information import connect
from detect_anomalies import detect
sys.path.append('sftp://ec2-52-207-83-62.compute-1.amazonaws.com/var/www/prediction')


# 9) If anomaly detected generate email
# 10) Run locally every 5 minutes to test
# 11) Make kron tab and integrate into webserver


# DevicesList field names - pID, sens_name, sens_serial, sens_location

DAYS_PRIOR = 14
tomorrows_date = datetime.now().date() + timedelta(days=1)
two_weeks_ago = tomorrows_date - timedelta(days=DAYS_PRIOR)


cursor = connect()
# Find what sensors are in the device list dynamically
sensor_code_select_sql = "SELECT sensor_serial,sensor_name, sensor_location FROM Devices;"
cursor.execute(sensor_code_select_sql)
sensor_codes = cursor.fetchall()

with open(os.path.dirname(__file__) + '/sensor_details.txt', 'w') as file:
    for sensor_code in sensor_codes:
        file.write("{},{},{}\n".format(sensor_code['sensor_serial'], sensor_code['sensor_name'], sensor_code['sensor_location']))

incomplete_sensor_details_select_sql = "SELECT sensor_date_time, sensor_temp FROM {} WHERE sensor_date_time BETWEEN '{}' AND '{}'"
# Select date and time from each sensor table
sensor_file_names = []
date_frame_header_names = ['ds','y']
for sensor_code in sensor_codes:
    complete_sensor_details_select_sql = incomplete_sensor_details_select_sql.format(sensor_code['sensor_serial'], two_weeks_ago, tomorrows_date)
    cursor.execute(complete_sensor_details_select_sql)
    sensor_data = cursor.fetchall()
    rows= []
    rows.append(date_frame_header_names)
    for row in range(len(sensor_data)):
        timestamp = sensor_data[row]['sensor_date_time']
        temp = sensor_data[row]['sensor_temp']
        entry = [timestamp, temp]
        rows.append(entry)
# write date and time into individual sensor csvs
    with open(os.path.dirname(__file__) + '/' +sensor_code['sensor_serial']+'.csv' ,'w') as file:
        sensor_file_names.append(sensor_code['sensor_serial'] + '.csv')
        writer = csv.writer(file)
        for entry in range(len(rows)):
            writer.writerow(rows[entry])


forecast_filenames = []

for sensor_file_name in sensor_file_names:
    historical_sensor_data = pd.read_csv(os.path.dirname(__file__) + '/' + sensor_file_name)

    # change first column to datetime
    historical_sensor_data['ds'] = pd.DatetimeIndex(historical_sensor_data['ds'])
    yesterday = datetime.now().date() - timedelta(days=1)
    # get all the data from yesterday to 2 weeks ago
    training_data = historical_sensor_data[(historical_sensor_data['ds'] < str(yesterday))]
    training_data.to_csv(os.path.dirname(__file__) + '/' + sensor_file_name, index_label=False, index=False, header=('Timestamp', 'Temps'))
    # get all the data
    testing_data = historical_sensor_data

    testing_model = Prophet(changepoint_prior_scale=0.01).fit(testing_data)
    # produce timestamps 4hrs into the future with 5 minute increments
    future_times = testing_model.make_future_dataframe(periods=48, freq='5min', include_history=False)
    # use the model to predict temps for these times
    forecast = testing_model.predict(future_times)

    # Write the date and temp to file
    forecast.to_csv(os.path.dirname(__file__) + '/Forecast-' + sensor_file_name, columns=('ds', 'yhat'), index_label=False, index=False,
                    header=('Timestamp', 'Temps'), float_format='%.2f')
    forecast_filenames.append(['Forecast-'+sensor_file_name])

with open(os.path.dirname(__file__) + '/sensor_forecast_filenames.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(forecast_filenames)

with open(os.path.dirname(__file__) + '/sensor_filenames.csv', 'w') as file:
    writer = csv.writer(file)
    for sensor_file_name in sensor_file_names:
        writer.writerow([sensor_file_name])

detect()





