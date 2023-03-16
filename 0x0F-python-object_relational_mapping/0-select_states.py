#!/usr/bin/python3

import sys
import MySQLdb

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

db = MySQLdb.Connect(host="localhost", port=3306,
                     user=username, passwd=password,
                     db=database)
cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY `id`")
rows = cur.fetchall()


for row in rows:
    print(row)
