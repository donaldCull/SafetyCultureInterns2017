select * from Devices;
select * FROM 49C2A9TH01;
select * FROM 4852F6TH01;
select * FROM 49C013TH01;

SHOW tables;
select * from Report;
SELECT UserID FROM Devices WHERE sensor_serial = "49C2A9TH01";
SELECT * from Users;
SELECT api_token FROM Users WHERE UserID = 1;
DROP TABLE Devices;
DROP TABLE Report;


INSERT INTO Devices (sensor_serial, UserID, sensor_name, sensor_location) VALUE ("49C013JH01", "2", "Food Fridge", "49C013TH01");
INSERT INTO Users (api_token, intervals) VALUE ("24DB3A5F73B12DC450FAF2718D78EB1B", "0,6,12,18")