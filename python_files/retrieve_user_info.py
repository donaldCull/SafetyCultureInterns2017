# A utility script for calling information from the Users table.

from connection_information import connect

cursor = connect()


def get_interval_times(user_id):
    sql_select_intervals_from_user = "SELECT intervals FROM Users WHERE UserID = {}".format(str(user_id))

    cursor.execute(sql_select_intervals_from_user)
    intervals = cursor.fetchall()
    # print(intervals[0]['intervals'].split(","))
    return intervals[0]['intervals'].split(",")


def get_api_token(user_id):
    sql_select_api_token_from_user = "SELECT api_token FROM Users WHERE UserID = {}".format(str(user_id))

    # print(sql_select_api_token_from_user)
    cursor.execute(sql_select_api_token_from_user)
    api_token = cursor.fetchall()
    # print(api_token)
    return api_token[0]['api_token']
