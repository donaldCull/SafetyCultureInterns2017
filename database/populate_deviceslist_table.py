import pymysql, requests, json

connection = pymysql.connect(host="sqldb2.cbu5ypzkmdln.ap-southeast-2.rds.amazonaws.com",
                             user="user", password="%T~wm]fK", db="sensorsData",
                             charset="utf8mb4",
                             cursorclass=pymysql.cursors.DictCursor, autocommit=True)

cursor = connection.cursor()

table_name = "DevicesList"
API_TOKEN = "24DB3A5F73B12DC450FAF2718D78EB1B"

request = requests.get('https://api.connectsense.com/v1/{}/devices'.format(API_TOKEN))
all_sensors = json.loads(request.text)
print(type(all_sensors))

# for sensor in all_sensors['serial_number']:
#     print(sensor)

#remove unnecessary sensor information
# response, sensor_scrap = request.text.split(",\"recent_reportings")

# add curly brace at the end of the string
# acceptable_string = response + "}"

# turn literal string into a dictionary
# sensor_details = json.loads(acceptable_string)

