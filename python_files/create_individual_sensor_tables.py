# Creates a table for each sensor for each User, pass in UserID

import utility_db_functions as udb

cursor = udb.connect()


def create_table(user_id):
    sensor_codes = udb.ListOfAllSensors(udb.get_api_token(user_id))

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
