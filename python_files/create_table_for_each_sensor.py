import retrieve_user_info
from python_files.connection_information import connect
from python_files.sensor_dictionaries import ListOfAllSensors

cursor = connect()

sensor_codes = ListOfAllSensors(retrieve_user_info.get_api_token("1"))

list_of_sql_queries = []

sql_incomplete = "CREATE TABLE " + \
                 "{}(pID int NOT NULL AUTO_INCREMENT, PRIMARY KEY (pID), " \
                 "sensor_date_time DATETIME, " \
                 "sensor_temp VARCHAR(5), " \
                 "sensor_humid VARCHAR(4));"

for sensor_codes in sensor_codes.values():
    list_of_sql_queries.append(sql_incomplete.format(sensor_codes))

# print(list_of_sql_queries)

for sql in list_of_sql_queries:
    print('Executing SQL query: "{}"'.format(sql))
    cursor.execute(sql)
