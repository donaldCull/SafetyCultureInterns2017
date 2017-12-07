import csv
# 1) Retrive sensor codes ***DONE
# 2) Select * from each sensor table - from oldest to newest ***Done
# 3) Save data to individual CSV's ***Done
# 4) Build model on each sensor data CSV
# 5) Make 5 minute predictions 4 hours into the future for each sensor
# 6) Save predictions into individual CSV's
# 7) Detect anomalies in each sensors prediction CSV
# 8) If anomaly detected generate incident report to be inserted into incident table
# 9) If anomaly detected generate email
# 10) Run locally every 5 minutes to test
# 11) Make kron tab and integrate into webserver

from database.connection_information import connect
# DevicesList field names - pID, sens_name, sens_serial, sens_location

cursor = connect()
sensor_code_select_sql = "SELECT sens_serial,sens_name, sens_location FROM DevicesList;"
cursor.execute(sensor_code_select_sql)
sensor_codes = cursor.fetchall()

# Sensor field names - pID, sensor_date_time, sensor_temp, sensor_humid
sensor_details_select_sql = "SELECT sensor_date_time, sensor_temp FROM {}"
for sensor_code in sensor_codes:
    cursor.execute(sensor_details_select_sql.format(sensor_code['sens_serial']))
    sensor_data = cursor.fetchall()
    rows= []
    for row in range(len(sensor_data)):
        timestamp = sensor_data[row]['sensor_date_time']
        temp = sensor_data[row]['sensor_temp']
        entry = [timestamp, temp]
        rows.append(entry)

    with open(sensor_code['sens_serial']+'.csv' ,'w') as file:
        writer = csv.writer(file)
        for entry in range(len(rows)):
            writer.writerow(rows[entry])

