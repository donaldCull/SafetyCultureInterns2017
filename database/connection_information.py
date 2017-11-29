import pymysql


def connect():
    connection = pymysql.connect(host="localhost", user="root", password="password", db="sensorsData",
                                 charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor, autocommit=True)

    return connection.cursor()
