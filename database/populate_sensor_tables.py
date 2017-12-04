import csv
from database.connection_information import connect

cursor = connect()
sensors = {"ambient_temp": "49C2A9TH01", "drinks_fridge": "4852F6TH01", "food_fridge": "49C013TH01"}
sql_partial = 'INSERT INTO ' + '{} (sensor_date_time, sensor_temp, sensor_humid) VALUE ("{}", "{}", "{}");'

# for sensor_code in sensors.values():
with open('../CSV/49C2A9TH01-Ambient-temp-altered.csv') as csvFile:
    readCSV = csv.reader(csvFile)
    # consumes header
    next(readCSV)
    for row in readCSV:
        date_time = row[0]
        temp = row[1]
        humidity = row[2]
        sql_command = sql_partial.format(sensors["ambient_temp"], date_time, temp,humidity)
        print(sql_command)
        cursor.execute(sql_command)
