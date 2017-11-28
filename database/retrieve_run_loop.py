import requests, time, json, datetime
import pymysql
run = True

previous_time = {}

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
    current_second = datetime.datetime.now().second

    # print(current_second)
    time.sleep(1)

    if current_second == 30 or current_second == 0:
        # print(current_second)

        #run retrieval code
        for sensor_code in sensors.values():
            #print('https://api.connectsense.com/v1/{}/devices/{}'.format(API_TOKEN, sensor_code))
            request = requests.get('https://api.connectsense.com/v1/{}/devices/{}'.format(API_TOKEN, sensor_code))

            response, sensor_scrap = request.text.split(",\"recent_reportings")
            acceptable_string = response + "}"
            sensor_individual_details = json.loads(acceptable_string)
            # print(sensor_individual_details)

            # print(sensor_individual_details)
            # previous_time[sensor_individual_details['serial_number']] = sensor_individual_details['last_reported_at']

            # print(sensor_individual_details['last_reported_at'])
            date, sensor_time = str(sensor_individual_details['last_reported_at']).split('T')
            # select only hh:mm:ss
            trimmed_time = sensor_time[0:8]
            cleaned_reported_date = (date, trimmed_time)
            # put back the new date and time as a tuple
            sensor_individual_details['last_reported_at'] = cleaned_reported_date

            print(int(cleaned_reported_date[1]))

            ###sql execution
            sql_execution_individual_sensor_table = 'INSERT INTO ' + sensor_code + ' (sens_serial, ' \
                                                                                   'sens_date, sens_time, ' \
                                                                                   'sens_temp, sens_humid)' \
                                                                                   ' VALUE ' \
                                                                                   '("{}", "{}", "{}", "{}", "{}");' \
                                                                                   ''.format(sensor_individual_details['serial_number'],
                                                                                             cleaned_reported_date[0],
                                                                                             cleaned_reported_date[1],
                                                                                             sensor_individual_details['temperature'],
                                                                                             sensor_individual_details['humidity'])
            print(sql_execution_individual_sensor_table)
            cursor.execute(sql_execution_individual_sensor_table)


        # print(previous_time)
