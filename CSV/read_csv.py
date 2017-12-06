# takes CSV data from connectSense which has a different time signature
# Changes the time to match DB date/time signature and writes to new CSV
import csv
from dateutil import parser
EMPTY = '--'
csv_filenames = ['49C2A9TH01-as-of-20171206.csv', '49C013TH01-as-of-20171206.csv', '4852F6TH01-as-of-20171206.csv']
altered_csv = []
for csv_filename in csv_filenames:
    with open(csv_filenames[0]) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        # Consume headers line
        next(readCSV)
        for row in readCSV:
            if row[1] != EMPTY and row[2] != EMPTY:
                # get date/time as correct format
                altered_time = parser.parse(row[0])
                # add the new time back into the row
                row[0] = altered_time
                altered_csv.append(row)


    with open("altered-" + csv_filename, 'w' ) as writeFile:
        csv_row_count = len(altered_csv)
        writer = csv.writer(writeFile)
        for row in range(csv_row_count - 1, -1, -1):
            writer.writerow(altered_csv[row])
        altered_csv.clear()
