#!/usr/bin/python3


'''
A script that lists all states with a name
starting with N from the database hbtn_0e_0_usa
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
                SELECT * FROM states
                WHERE name LIKE "N%"
                ORDER BY id
                ''')
    rows = cur.fetchall()
    if (len(rows) == 0):
        print()
    for row in rows:
        print(row)
