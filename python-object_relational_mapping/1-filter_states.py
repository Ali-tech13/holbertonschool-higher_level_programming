#!/usr/bin/python3
"""List all states whose names start with uppercase N."""

import sys

import MySQLdb


if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' "
        "ORDER BY id ASC"
    )

    for state in cursor.fetchall():
        print(state)

    cursor.close()
    conn.close()
