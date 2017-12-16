# Functions to call and receive data from db, usually pass in UserID to recieve data

import json

import pymysql
import requests


def connect():
    connection = pymysql.connect(host="mydbinstance.cizmyutwxzau.us-east-1.rds.amazonaws.com", user="user", password="p5TQHS360Hrk", db="SenseTemp",
                                 charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor, autocommit=True)

    return connection.cursor()


cursor = connect()


def GetIntervalTimes(user_id):
    sql_select_intervals_from_user = "SELECT intervals FROM Users WHERE UserID = {}".format(str(user_id))

    cursor.execute(sql_select_intervals_from_user)
    intervals = cursor.fetchall()
    # print(intervals[0]['intervals'].split(","))
    return intervals[0]['intervals'].split(",")


def GetApiToken(user_id):
    sql_select_api_token_from_user = "SELECT api_token FROM Users WHERE UserID = {}".format(str(user_id))

    # print(sql_select_api_token_from_user)
    cursor.execute(sql_select_api_token_from_user)
    api_token = cursor.fetchall()
    # print(api_token)
    return api_token[0]['api_token']


# Returns all sensors from API for user specified (by passing in their api_token)
def ListOfAllSensors(api_token):
    sensor = {}
    api_url = 'https://api.connectsense.com/v1/{}/devices/'.format(api_token)
    request = requests.get(api_url, timeout=20)

    dictionary_from_requests = json.loads(request.text)

    # print(dictionary_from_requests)

    for i, e in enumerate(dictionary_from_requests):
        if 'temperature' in e:
            # print(dictionary_from_requests[i]['name'])
            # print(dictionary_from_requests[i]['serial_number'])
            sensor[dictionary_from_requests[i]['name']] = dictionary_from_requests[i]['serial_number']

    # print(sensor)
    return sensor


# Used for generating reports
def ListOfUserSensors(user_id):
    sql_query_users_devices = "SELECT sensor_serial, sensor_name FROM Devices WHERE UserID = {}".format(user_id)
    cursor.execute(sql_query_users_devices)
    sensors = cursor.fetchall()
    return_sensor = {}

    for sensor in sensors:
        return_sensor[sensor['sensor_name']] = sensor['sensor_serial']

    print(return_sensor)
    return return_sensor


def ListOfAllUsers():
    sql_retrieve_user_list = "SELECT UserID FROM Users"

    cursor.execute(sql_retrieve_user_list)
    all_users = cursor.fetchall()
    # print(type(all_users))
    return all_users
