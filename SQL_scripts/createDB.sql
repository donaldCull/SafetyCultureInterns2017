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
    report_location VARCHAR(1000)
);