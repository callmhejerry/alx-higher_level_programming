#!/usr/bin/python3


'''
A script that takes in the name of a state as
an argument and lists all cities of that state,
using the database hbtn_0e_4_usa
'''


if __name__ == "__main__":
    import sys
    import MySQLdb

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.Connect(host="localhost", port=3306,
                         user=username, passwd=password,
                         db=database)
    cur = db.cursor()
    state_name = sys.argv[4]
    cur.execute('''
                SELECT name
                FROM cities
                WHERE state_id = (
                    SELECT id
                    FROM states
                    WHERE name = %s
                )
                ''', (state_name, ))
    rows = cur.fetchall()
    my_str = ''
    for item in range(len(rows)):
        (city,) = rows[item]
        if (item != len(rows) - 1):
            my_str = my_str + "{}, ".format(city)
        else:
            my_str = my_str + city

    print(my_str)
