# takes CSV data from connectSense which has a different time signature
# Changes the time to match DB date/time signature and writes to new CSV
import csv
from dateutil import parser
altered_csv = []
with open('4852F6TH01-Drinks-fridge.csv') as csvfile:

    readCSV = csv.reader(csvfile, delimiter=',')
    # Consume headers line
    altered_csv.append(next(readCSV))
    for row in readCSV:
        # get date/time as correct format
        altered_time = parser.parse(row[0])
        # add the new time back into the row
        row[0] = altered_time
        altered_csv.append(row)


with open('4852F6TH01-Drinks-fridge-altered.csv', 'w' ) as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(altered_csv)
