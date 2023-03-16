#!/usr/bin/python3


'''
A script that lists all the cities from the
database hbtn_0e_4_usa
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
    cur.execute('''
                SELECT cities.id, cities.name, states.name
                FROM cities
                JOIN states ON cities.state_id = states.id
                ''',)
    rows = cur.fetchall()

    for row in rows:
        print(row)
