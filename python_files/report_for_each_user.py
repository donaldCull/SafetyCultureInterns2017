# Looping through each user and generating the last weeks report.

from python_files import report_generator, connect_to_db

sql_retrieve_user_list = "SELECT UserID FROM Users"
cursor = connect_to_db.connect()

cursor.execute(sql_retrieve_user_list)
users = cursor.fetchall()

for dictionary in users:
    # print(dictionary)
    report_generator.generate_report(dictionary['UserID'])


# TODO: MERGE INTO REPORT GENERATOR FILE