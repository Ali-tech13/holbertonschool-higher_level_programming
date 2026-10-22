#!/usr/bin/python3
"""List states matching a name provided by the user."""

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

    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
    cursor.execute(query.format(sys.argv[4]))

    for state in cursor.fetchall():
        print(state)

    cursor.close()
    conn.close()
