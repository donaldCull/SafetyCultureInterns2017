#INSERT INTO Incidents(incid_serial, incid_location, incid_name, incid_date_start, incid_time_start, incid_temp, incid_date_stop, incid_time_stop) VALUES ("49C013TH01","Kitchen","Food Fridge","2017-11-16","09:56:11","9.5","2017-11-16","10:08:12");
#INSERT INTO Incidents(incid_serial, incid_location, incid_name, incid_date_start, incid_time_start, incid_temp, incid_date_stop, incid_time_stop) VALUES ("4852F6TH01","Kitchen","Drinks Fridge","2017-11-17","10:56:11","5","2017-11-18","11:08:12");



#INSERT INTO Report(report_date, report_json) VALUE ("1233-03-09", '"Report_1":{"Sensor_1":{"Monday":[1.2,3.7,4.3,5.5], "Tuesday":[1.2,3.7,4.3,5.5], "Wednsday":[1.2,3.7,4.3,5.5], "Thursday":[1.2,3.7,4.3,5.5], "Friday":[1.2,3.7,4.3,5.5], "Saturday":[1.2,3.7,4.3,5.5], "Sunday":[1.2,3.7,4.3,5.5]}, "Sensor_2":{"Monday":[1.2,3.7,4.3,5.5], "Tuesday":[1.2,3.7,4.3,5.5], "Wednsday":[1.2,3.7,4.3,5.5], "Thursday":[1.2,3.7,4.3,5.5], "Friday":[1.2,3.7,4.3,5.5], "Saturday":[1.2,3.7,4.3,5.5], "Sunday":[1.2,3.7,4.3,5.5]}, "Sensor_3":{"Monday":[1.2,3.7,4.3,5.5], "Tuesday":[1.2,3.7,4.3,5.5], "Wednsday":[1.2,3.7,4.3,5.5], "Thursday":[1.2,3.7,4.3,5.5], "Friday":[1.2,3.7,4.3,5.5], "Saturday":[1.2,3.7,4.3,5.5], "Sunday":[1.2,3.7,4.3,5.5]}}');
#INSERT INTO 4852F6TH01(sensor_date, sensor_time, sens_temp, sens_humid) VALUE ("12-19-1999", "19:19:19", "1.6", "5.6");
#SELECT * FROM Report;
select * FROM 49C2A9TH01;
select * FROM 4852F6TH01;
select * FROM 49C013TH01;
#select * from DevicesList;

#SHOW TABLES

#DROP TABLE 49C2A9TH01;
#DROP TABLE 4852F6TH01;
#DROP TABLE 49C013TH01;

#select * from Incidents;
#DROP TABLES Incidents

#select * from Incidents;


