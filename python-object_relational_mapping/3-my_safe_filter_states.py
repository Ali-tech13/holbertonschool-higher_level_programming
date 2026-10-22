#!/usr/bin/python3
"""Display states matching a name safely using MySQLdb."""

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

    query = (
        "SELECT * FROM states WHERE name = BINARY %s "
        "ORDER BY id ASC"
    )
    cursor.execute(query, (sys.argv[4],))

    for state in cursor.fetchall():
        print(state)

    cursor.close()
    conn.close()
