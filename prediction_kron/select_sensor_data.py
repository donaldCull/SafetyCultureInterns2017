import csv
import pandas as pd
from fbprophet import Prophet
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

# 1) Retrive sensor codes ***DONE
# 2) Select * from each sensor table - from oldest to newest ***Done
# 3) Save data to individual CSV's ***Done
# 4) Build model on each sensor data CSV ***DONe
# 5) Make 5 minute predictions 4 hours into the future for each sensor ***DOne
# 6) Save predictions into individual CSV's *** DONE
# 7) Detect anomalies in each sensors prediction CSV ***DONe
# 8) If anomaly detected generate incident report to be inserted into incident table
# 9) If anomaly detected generate email
# 10) Run locally every 5 minutes to test
# 11) Make kron tab and integrate into webserver

from database.connection_information import connect
# DevicesList field names - pID, sens_name, sens_serial, sens_location

cursor = connect()
# Find what sensors are in the device list dynamically
sensor_code_select_sql = "SELECT sens_serial,sens_name, sens_location FROM DevicesList;"
cursor.execute(sensor_code_select_sql)
sensor_codes = cursor.fetchall()

with open('sensor_details.txt', 'w') as file:
    for sensor_code in sensor_codes:
        file.write("{},{},{}\n".format(sensor_code['sens_serial'], sensor_code['sens_name'], sensor_code['sens_location']))

# Sensor field names - pID, sensor_date_time, sensor_temp, sensor_humid
sensor_details_select_sql = "SELECT sensor_date_time, sensor_temp FROM {}"
# Select date and time from each sensor table
sensor_file_names = []
date_frame_header_names = ['ds','y']
for sensor_code in sensor_codes:
    cursor.execute(sensor_details_select_sql.format(sensor_code['sens_serial']))
    sensor_data = cursor.fetchall()
    rows= []
    rows.append(date_frame_header_names)
    for row in range(len(sensor_data)):
        timestamp = sensor_data[row]['sensor_date_time']
        temp = sensor_data[row]['sensor_temp']
        entry = [timestamp, temp]
        rows.append(entry)
# write date and time into individual sensor csvs
    with open(sensor_code['sens_serial']+'.csv' ,'w') as file:
        sensor_file_names.append(sensor_code['sens_serial'] + '.csv')
        writer = csv.writer(file)
        for entry in range(len(rows)):
            writer.writerow(rows[entry])


forecast_filenames = []

for sensor_file_name in sensor_file_names:
    data_frame = pd.read_csv(sensor_file_name)
    # change first column to datetime
    data_frame['ds'] = pd.DatetimeIndex(data_frame['ds'])

    # make a plot of the historical data
    # threshold needs to be extracted from user preferences
    threshold = 5.0
    ax = data_frame.set_index('ds').plot(figsize=(12, 8))

    # Provide a way to use these graphs on the website
    # add a threshold line to historical data vis
    ax.axhline(y=threshold, color='r', linestyle='-')
    ax.set_ylabel('Temperature recordings')
    ax.set_xlabel('DateTime')

    model = Prophet(changepoint_prior_scale=0.01).fit(data_frame)
    # produce 300 future timestamps in 5 minute increments
    future_times = model.make_future_dataframe(periods=48, freq='5min', include_history=False)
    # use the model to predict temps for these times
    forecast = model.predict(future_times)

    # predictions stored in a csv file and overwritten each time? Or update a database with predictions
    # Write the date and temp to file
    forecast.to_csv('Forecast-'+sensor_file_name, columns=('ds', 'yhat'), index_label=False, index=False,
                    header=('Timestamp', 'Temps'), float_format='%.2f')
    forecast_filenames.append(['Forecast-'+sensor_file_name])
    # display the last 5 observations and their predicted temps with upper and lower boundaries
    # print()
    # print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())

    # plot the forecast results
    model.plot(forecast, uncertainty=True)
    # plot the overall and daily trend
    model.plot_components(forecast)

with open('sensor_forecast_filenames.csv' ,'w') as file:
    writer = csv.writer(file)
    writer.writerows(forecast_filenames)

with open('sensor_filenames.csv', 'w') as file:
    writer = csv.writer(file)
    for sensor_file_name in sensor_file_names:
        writer.writerow([sensor_file_name])

# plt.show()




