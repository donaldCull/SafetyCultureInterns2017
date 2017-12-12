import csv

from prediction_kron.connection_information import connect

csv_filename = 'altered-4852F6TH01-as-of-20171212.csv'
table_name = '4852F6TH01'
import python_files.utility_db_functions as udb
cursor = udb.connect()
sql_partial = 'INSERT INTO ' + '{} (sensor_date_time, sensor_temp, sensor_humid) VALUE ("{}", "{}", "{}");'
with open('../CSV/' + csv_filename) as csvFile:
    readCSV = csv.reader(csvFile)
    for row_count, row in enumerate(readCSV):
        date_time = row[0]
        temp = row[1]
        humidity = row[2]
        sql_command = sql_partial.format(table_name, date_time, temp,humidity)
        print("row: {} - {}".format(row_count, sql_command))
        cursor.execute(sql_command)
