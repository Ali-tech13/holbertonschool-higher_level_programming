#!/usr/bin/python3
"""List all cities with their corresponding states from MySQL."""

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
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )

    cursor.execute(query)

    for city in cursor.fetchall():
        print(city)

    cursor.close()
    conn.close()
