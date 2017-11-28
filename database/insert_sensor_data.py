import pymysql

from database.retreive_API_sensor_data import fetch


def main():
    table = "RawData"

    connection = pymysql.connect(host="tutorial-db-instance.cbu5ypzkmdln.ap-southeast-2.rds.amazonaws.com", user="tutorial_user", password="pjq6aMsMC8FX", db="sample",
                                 charset="utf8mb4",
                                 cursorclass=pymysql.cursors.DictCursor, autocommit=True)
    cursor = connection.cursor()
    sensors = fetch()
    for sensor in sensors:
        date, time = str(sensor['last_reported_at']).split('T')
        # select only hh:mm:ss
        trimmed_time = time[0:8]
        cleaned_reported_date = (date, trimmed_time)
        # put back the new date and time as a tuple
        sensor['last_reported_at'] = cleaned_reported_date

        sql = 'INSERT INTO ' + table + ' (sens_name, sens_serial, sens_location, sens_date, sens_time, sens_temp, sens_humid)' \
                                       ' VALUE ("{}", "{}", "{}", "{}", "{}", "{}", "{}");'.format(sensor['name'],
                                                                                                   sensor['serial_number'],
                                                                                                   sensor['location'],
                                                                                                   sensor['last_reported_at'][0],
                                                                                                   sensor['last_reported_at'][1],
                                                                                                   sensor['temperature'],
                                                                                                   sensor['humidity'])

        print(sql)
        cursor.execute(sql)
main()