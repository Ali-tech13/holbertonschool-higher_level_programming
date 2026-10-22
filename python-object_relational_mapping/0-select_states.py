#!/usr/bin/python3
"""List all states from a MySQL database"""
import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

cursor = conn.cursor()
cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
states = cursor.fetchall()

for state in states:
    print(state)

cursor.close()
conn.close()
