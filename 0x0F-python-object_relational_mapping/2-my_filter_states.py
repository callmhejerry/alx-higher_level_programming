#!/usr/bin/python3


'''
A script that takes in an arguement and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument
'''


if __name__ == "__main__":
    import sys
    import MySQLdb

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    args = sys.argv[4]

    db = MySQLdb.Connect(host="localhost", port=3306,
                         user=username, passwd=password,
                         db=database)
    cur = db.cursor()
    cur.execute('''
                SELECT * FROM states
                WHERE name LIKE BINARY '{}'
                ORDER BY id
                '''.format(args))
    rows = cur.fetchall()

    for row in rows:
        print(row)
