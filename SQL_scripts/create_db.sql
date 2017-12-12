DROP DATABASE SenseTemp;
CREATE DATABASE SenseTemp;
USE SenseTemp;

CREATE TABLE Devices(
	sensor_serial VARCHAR(10) NOT NULL, PRIMARY KEY (sensor_serial),
    UserID INT NOT NULL,
	sensor_name VARCHAR(20),
    sensor_location VARCHAR(20)
);

CREATE TABLE Users(
	UserID INT NOT NULL AUTO_INCREMENT, PRIMARY KEY (UserID),
    api_token VARCHAR(50),
    intervals VARCHAR(11)
);

CREATE TABLE Report(
	Report_ID INT NOT NULL AUTO_INCREMENT, PRIMARY KEY (Report_ID),
    UserID INT NOT NULL,
    report_date VARCHAR(10),
    report_json VARCHAR(10000)
);

CREATE TABLE Incident(
	incid_ID INT NOT NULL AUTO_INCREMENT, PRIMARY KEY (incid_ID),
    incid_serial VARCHAR(10),
    incid_location VARCHAR(20),
    incid_name VARCHAR (20),
    incid_date_start VARCHAR(10),
    incid_time_start VARCHAR(8),
    incid_temp VARCHAR(5)
);