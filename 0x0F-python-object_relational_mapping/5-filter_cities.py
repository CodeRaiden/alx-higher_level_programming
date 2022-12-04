#!/usr/bin/python3
"""
Script that takes in name of state as argument and list
all cities of that state
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    conn = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    check = (argv[4], )
    cur.execute("SELECT * FROM cities JOIN states\
    ON cities.state_id = states.id WHERE states.name = %s\
    ORDER BY cities.id ASC", check)
    sts = cur.fetchall()
    cities = []
    for row in sts:
        if row[4] == check[0]:
            cities.append(row[2])
    print(', '.join(cities))
    cur.close()
    conn.close()
