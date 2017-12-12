# Looping through each user and generating the last weeks report.

import report_generator
import utility_db_functions as udb

sql_retrieve_user_list = "SELECT UserID FROM Users"
cursor = udb.connect()

cursor.execute(sql_retrieve_user_list)
users = cursor.fetchall()

for dictionary in users:
    # print(dictionary)
    report_generator.generate_report(dictionary['UserID'])

# TODO: MERGE INTO REPORT GENERATOR FILE
