# Looping through each user and generating the last weeks report.

from python_files import report_generator, connection_information

sql_retrieve_user_list = "SELECT UserID FROM Users"
cursor = connection_information.connect()

cursor.execute(sql_retrieve_user_list)
result = cursor.fetchall()
# print(result)

for dictionary in result:
    report_generator.generate_report(dictionary['UserID'])
