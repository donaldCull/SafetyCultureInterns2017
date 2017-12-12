# Importing historic data into the database's device tables

import csv

import utility_db_functions as udb

csv_filenames = ['altered-49C2A9TH01-as-of-20171206.csv', 'altered-49C013TH01-as-of-20171206.csv',
                 'altered-4852F6TH01-as-of-20171206.csv']
table_names = ['49C2A9TH01', '49C013TH01', '4852F6TH01']

cursor = udb.connect()
sql_partial = 'INSERT INTO ' + '{} (sensor_date_time, sensor_temp, sensor_humid) VALUE ("{}", "{}", "{}");'
table_count = 0
for csv_filename in csv_filenames:
    with open('../CSV/' + csv_filename) as csvFile:
        readCSV = csv.reader(csvFile)
        for row_count, row in enumerate(readCSV):
            date_time = row[0]
            temp = row[1]
            humidity = row[2]
            sql_command = sql_partial.format(table_names[table_count], date_time, temp, humidity)
            print("row: {} - {}".format(row_count, sql_command))
            cursor.execute(sql_command)
    table_count += 1
    print()
