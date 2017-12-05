import csv
extracted_data = []
with open('../CSV/49C2A9TH01-Ambient-temp-altered.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        extracted_data.append(row[0:2])

extracted_data_length = len(extracted_data)
print(extracted_data_length)
with open('data.csv', 'w') as writefile:
    writeCSV = csv.writer(writefile)
    # writes to file from oldest to newest
    for row in range(extracted_data_length - 1, 0, -1):
        print(extracted_data[row])
        writeCSV.writerow(extracted_data[row])
