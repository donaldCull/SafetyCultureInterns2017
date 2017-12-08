INSERT INTO Incidents(incid_serial, incid_location, incid_name, incid_date_start, incid_time_start, incid_temp, incid_date_stop, incid_time_stop) VALUES ("49C013TH01","Kitchen","Food Fridge","2017-11-16","09:56:11","9.5","2017-11-16","10:08:12");
INSERT INTO Incidents(incid_serial, incid_location, incid_name, incid_date_start, incid_time_start, incid_temp, incid_date_stop, incid_time_stop) VALUES ("4852F6TH01","Kitchen","Drinks Fridge","2017-11-17","10:56:11","5","2017-11-18","11:08:12");
INSERT INTO Incidents(incid_serial, incid_location, incid_name, incid_date_start, incid_time_start, incid_temp, incid_date_stop, incid_time_stop) VALUES ("4852F6TH02","Kitchen","Bar Fridge","2017-01-07","10:23:23","7.1","2017-01-07","10:34:54");
INSERT INTO Incidents(incid_serial, incid_location, incid_name, incid_date_start, incid_time_start, incid_temp, incid_date_stop, incid_time_stop) VALUES ("4852F6TH02","Kitchen","Walkin Fridge","2017-08-12","10:45:11","5.2","2017-08-12","10:55:34");
-- 
SELECT * FROM Incidents;
-- 
-- 
DROP TABLE Report;
-- SELECT * FROM Report;
 
INSERT INTO 49C013TH01(sensor_date_time, sensor_temp, sensor_humid) VALUE ("2017-12-03 00:00:00", "9.9", "5.6");
INSERT INTO 49C013TH01(sensor_date_time, sensor_temp, sensor_humid) VALUE ("2017-12-03 06:00:00", "8.9", "5.6");
INSERT INTO 49C013TH01(sensor_date_time, sensor_temp, sensor_humid) VALUE ("2017-12-03 12:00:00", "7.9", "5.6");
INSERT INTO 49C013TH01(sensor_date_time, sensor_temp, sensor_humid) VALUE ("2017-12-03 18:00:00", "6.9", "5.6");


INSERT INTO Report(report_date, report_json) VALUE ("2017-12-06", "{'49C2A9TH01': {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': [], 'Saturday': [], 'Sunday': []}, '4852F6TH01': {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': [], 'Saturday': [], 'Sunday': []}, '49C013TH01': {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': [], 'Saturday': [], 'Sunday': []}, 'Dates': ['2017-11-29', '2017-11-30', '2017-12-01', '2017-12-02', '2017-12-03', '2017-12-04', '2017-12-05'], 'Times': [0, 6, 12, 18]}");

SELECT * FROM Report;
select * FROM 49C2A9TH01;
select * FROM 4852F6TH01;
select * FROM 49C013TH01;
select * from DevicesList;


INSERT INTO Report(report_date, report_json) VALUE ('2017-12-06','{'49C2A9TH01': {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': [], 'Saturday': [], 'Sunday': []}, '4852F6TH01': {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': [], 'Saturday': [], 'Sunday': []}, '49C013TH01': {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': [], 'Saturday': [], 'Sunday': []}, 'Dates': ['2017-11-29', '2017-11-30', '2017-12-01', '2017-12-02', '2017-12-03', '2017-12-04', '2017-12-05'], 'Times': [0, 6, 12, 18]}')

#SHOW TABLES

#DROP TABLE 49C2A9TH01;
#DROP TABLE 4852F6TH01;
#DROP TABLE 49C013TH01;

#select * from Incidents;
#DROP TABLES Incidents

#select * from Incidents;

SELECT * FROM 49C2A9TH01 WHERE sensor_date_time BETWEEN '2017-11-29' AND '2017-12-06';
-- SELECT * FROM 49C2A9TH01 WHERE sensor_date BETWEEN '2017-12-01 00:00:00' AND '2017-11-24 00:00:00';
-- SELECT * FROM 49C2A9TH01 WHERE sensor_date BETWEEN '2017-12-01' AND '2017-11-24';
-- SELECT * FROM 49C013TH01 WHERE sensor_date BETWEEN '2017-11-24' AND '2017-12-01';