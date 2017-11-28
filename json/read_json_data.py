import json

with open("cleaned_sensor_data.json","r") as file:
  sensors = json.load(file)

for sensor in sensors:
    print(sensor)