import pymysql

connection = pymysql.connect(host="localhost",
                             user="root", password="password", db="sensorsData",
                             charset="utf8mb4",
                             cursorclass=pymysql.cursors.DictCursor, autocommit=True)

cursor = connection.cursor()

sensor_codes = {"ambient_temp": "49C2A9TH01", "drinks_fridge": "4852F6TH01", "food_fridge": "49C013TH01"}

list_of_sql_queries = []

sql_incomplete = "CREATE TABLE " + \
              "{}(pID int NOT NULL AUTO_INCREMENT, PRIMARY KEY (pID), " \
              "sensor_date VARCHAR(10), " \
              "sensor_time VARCHAR(8), " \
              "sens_temp VARCHAR(5), " \
              "sens_humid VARCHAR(4));"


for sensor_codes in sensor_codes.values():
    list_of_sql_queries.append(sql_incomplete.format(sensor_codes))

# print(list_of_sql_queries)

for sql in list_of_sql_queries:
    print('Executing SQL query: "{}"'.format(sql))
    cursor.execute(sql)
