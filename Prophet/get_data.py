import csv
extracted_data = []
with open('../CSV/49C2A9TH01-Ambient-temp-altered.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        extracted_data.append(row[0:2])

with open('data.csv', 'w') as writefile:
    writeCSV = csv.writer(writefile)
    writeCSV.writerows(extracted_data)
