import csv
from dateutil import parser


threshold = 5.0

with open('Predict_Output') as file:
    readFile = csv.reader(file)
    next(file)
    for row in readFile:
        # threshold comparision is arbitrarily chosen
        if float(row[1]) <= threshold:
            timestamp = parser.parse(row[0])
            print("Anomaly Detected: On {} at {} with a temperature of {}".format(timestamp.date(), timestamp.time(), row[1]))
            message = "Anomaly Detected: On {} at {} with a temperature of {}".format(timestamp.date(), timestamp.time(), row[1])
            with open('email_alert', 'w') as file:
                writer = file.write(message)

