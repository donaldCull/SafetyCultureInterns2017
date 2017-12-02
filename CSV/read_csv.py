import csv
from dateutil import parser
altered_csv = []
with open('49C2A9TH01-Ambient-temp.csv') as csvfile:

    readCSV = csv.reader(csvfile, delimiter=',')
    # Consume headers line
    next(readCSV)
    for row in readCSV:
        # get date/time as correct format
        altered_time = parser.parse(row[0])
        # add the new time back into the row
        row[0] = altered_time
        altered_csv.append(row)


with open('49C2A9TH01-Ambient-temp-altered.csv', 'w' ) as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(altered_csv)

# print(row1)
# print(row2)
# date = row2[0]
# dt = parser.parse(date)
# # extract_date = arrow.get(date, 'YYYY-MMM-DD HH:mm:ss')
# # extract_date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
# print(date)
# print(dt)
