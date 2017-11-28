import pymysql, requests, json

API_TOKEN = "24DB3A5F73B12DC450FAF2718D78EB1B"
sensors = {"ambient_temp": "49C2A9TH01", "drinks_fridge": "4852F6TH01", "food_fridge": "49C013TH01"}
sql_partial = 'INSERT INTO ' + '{} (sens_name, sens_serial, sens_location) VALUE ("{}", "{}", "{}");'

connection = pymysql.connect(host="sqldb2.cbu5ypzkmdln.ap-southeast-2.rds.amazonaws.com",
                             user="user", password="%T~wm]fK", db="sensorsData",
                             charset="utf8mb4",
                             cursorclass=pymysql.cursors.DictCursor, autocommit=True)

cursor = connection.cursor()

for sensor_code in sensors.values():
    # print('https://api.connectsense.com/v1/{}/devices/{}'.format(API_TOKEN, sensor_code))
    request = requests.get('https://api.connectsense.com/v1/{}/devices/{}'.format(API_TOKEN, sensor_code))

    response, sensor_scrap = request.text.split(",\"recent_reportings")
    acceptable_string = response + "}"
    sensor_individual_details = json.loads(acceptable_string)
    #print(sensor_individual_details)

    sql_command = sql_partial.format("DevicesList", sensor_individual_details['name'], sensor_code, sensor_individual_details['location'])
    print(sql_command)
    cursor.execute(sql_command)
