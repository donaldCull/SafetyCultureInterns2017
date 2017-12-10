DROP DATABASE sensorsData;
CREATE DATABASE sensorsData; 
USE sensorsData;

CREATE TABLE DevicesList(
	pID int NOT NULL AUTO_INCREMENT, PRIMARY KEY (pID),
    sens_name VARCHAR(20),
    sens_serial VARCHAR(10),
    sens_location VARCHAR(20)
);

CREATE TABLE Report(
	pID int NOT NULL AUTO_INCREMENT, PRIMARY KEY (pID),
    report_date VARCHAR(10),
    report_json VARCHAR(2000)	#string of cvs location, buld strings are bad form and files are impossible
);

CREATE TABLE Incidents(
	pID int NOT NULL AUTO_INCREMENT, PRIMARY KEY (pID),
    incid_serial VARCHAR(10),
    incid_location VARCHAR(20),
    incid_name VARCHAR (20),
    incid_date_start VARCHAR(10),
    incid_time_start VARCHAR(8),
    incid_temp VARCHAR(5),
);