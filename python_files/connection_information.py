# Contains database connection information
# Call connection_information.connect() to establish connection

import pymysql


def connect():
    connection = pymysql.connect(host="localhost", user="root", password="password", db="SenseTemp",
                                 charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor, autocommit=True)

    return connection.cursor()
