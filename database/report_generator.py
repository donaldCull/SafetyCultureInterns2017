import datetime
from dateutil.parser import parse
import arrow
from connection_information import connect


cursor = connect()

sensors = {"ambient_temp": "49C2A9TH01", "drinks_fridge": "4852F6TH01", "food_fridge": "49C013TH01"}

sql_get_dates_incomplete = "SELECT * FROM {} WHERE sensor_date BETWEEN '{}' AND '{}';"

last_weeks_data = ""

todays_date = arrow.now().date()
seven_days_ago = todays_date - datetime.timedelta(days=7)

list_of_values = {}

for sensor_code in sensors.values():
    list_of_values[sensor_code] = []

for sensor_code in sensors.values():
    sql_to_execute = sql_get_dates_incomplete.format(sensor_code, seven_days_ago, todays_date)
    # print(sql_to_execute)
    list_of_values[sensor_code] = cursor.execute(sql_to_execute)
    print(list_of_values)


print(last_weeks_data)
