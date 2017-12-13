import pymysql


def connect():
    connection = pymysql.connect(host="mydbinstance.cizmyutwxzau.us-east-1.rds.amazonaws.com", user="user", password="p5TQHS360Hrk", db="SenseTemp",
                                 charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor, autocommit=True)

    return connection.cursor()
