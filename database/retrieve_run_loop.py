import requests, time, json, datetime
import pymysql

run = True
timezone_adjustment = 2

previous_time = {}

five_minute_intervals = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55]

API_TOKEN = "24DB3A5F73B12DC450FAF2718D78EB1B"
sensors = {"ambient_temp": "49C2A9TH01", "drinks_fridge": "4852F6TH01", "food_fridge": "49C013TH01"}

connection = pymysql.connect(host="sqldb2.cbu5ypzkmdln.ap-southeast-2.rds.amazonaws.com",
                             user="user", password="%T~wm]fK", db="sensorsData",
                             charset="utf8mb4",
                             cursorclass=pymysql.cursors.DictCursor, autocommit=True)

cursor = connection.cursor()

for sensor_code in sensors.values():
    previous_time[sensor_code] = ''

while run:
    # current_second = datetime.datetime.now().second
    current_minute = datetime.datetime.now().minute

    print(current_minute)


    # if current_second == 0 or current_second == 30:
    if current_minute in five_minute_intervals:
        # print(current_second)

        # run retrieval code
        for sensor_code in sensors.values():
            # print('https://api.connectsense.com/v1/{}/devices/{}'.format(API_TOKEN, sensor_code))
            request = requests.get('https://api.connectsense.com/v1/{}/devices/{}'.format(API_TOKEN, sensor_code))

            response, sensor_scrap = request.text.split(",\"recent_reportings")
            acceptable_string = response + "}"
            sensor_individual_details = json.loads(acceptable_string)
            # print(sensor_individual_details)

            # print(sensor_individual_details)
            # previous_time[sensor_individual_details['serial_number']] = sensor_individual_details['last_reported_at']

            server_side_reported_date = datetime.datetime.now()
            # print(server_side_reported_date)

            server_side_reported_date -= datetime.timedelta(hours=timezone_adjustment)

            req_date, req_time = str(server_side_reported_date).split(" ")

            # put back the new date and time as a tuple
            sensor_individual_details['last_reported_at'] = server_side_reported_date

            # print(int(cleaned_reported_date[1]))

            ###sql execution
            sql_execution_individual_sensor_table = 'INSERT INTO ' + sensor_code + ' (sens_serial, ' \
                                                                                   'retrieved_date, retrieved_time, ' \
                                                                                   'sens_temp, sens_humid)' \
                                                                                   ' VALUE ' \
                                                                                   '("{}", "{}", "{}", "{}", "{}");' \
                                                                                   ''.format(
                sensor_individual_details['serial_number'],
                req_date,
                req_time,
                sensor_individual_details['temperature'],
                sensor_individual_details['humidity'])
            print(sql_execution_individual_sensor_table)
            cursor.execute(sql_execution_individual_sensor_table)

            # print(current_second)
    time.sleep(60)
