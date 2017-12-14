import sys
from connection_information import connect
from datetime import timedelta
import pandas as pd
from fbprophet import Prophet
from suppress_prophet_output import suppress_stdout_stderr


sys.path.append('sftp://ec2-52-207-83-62.compute-1.amazonaws.com/var/www/prediction')
# start retrieve sensor data
cursor = connect()

get_user_sensors_sql = "SELECT sensor_serial, sensor_name, sensor_location, min_threshold, max_threshold FROM Devices;"
cursor.execute(get_user_sensors_sql)
sensor_details = cursor.fetchall()
for sensor, sensor_serial_code in enumerate(sensor_details):
    get_sensor_data_sql = "SELECT sensor_date_time, sensor_temp FROM {};".format(sensor_serial_code['sensor_serial'])
    cursor.execute(get_sensor_data_sql)
    raw_sensor_data = cursor.fetchall()
    historical_sensor_data = pd.DataFrame(raw_sensor_data)
    historical_sensor_data['sensor_date_time'] = pd.DatetimeIndex(historical_sensor_data['sensor_date_time'])
    historical_sensor_data['sensor_temp'] = pd.to_numeric(historical_sensor_data['sensor_temp'])
    training_data = historical_sensor_data.rename(columns={'sensor_date_time': 'ds',
                            'sensor_temp': 'y'})
    with suppress_stdout_stderr():
        #https://facebook.github.io/prophet/docs/non-daily_data.html
        model = Prophet(changepoint_prior_scale=0.01).fit(training_data)
    future_times = model.make_future_dataframe(periods=48, freq='5min', include_history=False)
    forecast = model.predict(future_times)
    anomalies = []
    for index, row in forecast.iterrows():
        # check if there is anomaly
        if float(row['yhat']) >= sensor_serial_code['min_threshold'] and float(row['yhat']) <= sensor_serial_code['max_threshold']:
            anomalies.append([row['ds'],row['yhat']])
    if len(anomalies) != 0:
        anomaly_start = anomalies[0][0]
        anomaly_start_temp = anomalies[0][1]
        anomaly_end = anomalies[-1][0]
        anomaly_end_temp = anomalies[-1][1]
        time_period = anomaly_start + timedelta(hours=3)
        if anomaly_end >= time_period:
            print("Sensor {} ({}) location {} anomaly predicted beginning at {} with a temperature of {:.2f} and ending at {} with a temperature of {:.2f}".format(sensor_serial_code['sensor_name'], sensor_serial_code['sensor_serial'],
                                                                                                                                              sensor_serial_code['sensor_location'],anomaly_start,anomaly_start_temp,
                                                                                                                                                          anomaly_end, anomaly_end_temp))
        anomalies.clear()

