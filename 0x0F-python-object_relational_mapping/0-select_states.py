#!/usr/bin/python3


import MySQLdb
from sys import argv

'''
a script that lists all states
from the database
'''
if __name__ == "__main__":
    con = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1],
        password=argv[2]cursor.execute("SELECT * FROM states ORDER BY id A, database=argv[3])
    cursor = con.cursor()
    SC")
    db = cursor.fetchall()
    for i in db:
        print(i)
    cursor.close()
    db.close()
