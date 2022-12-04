#!/usr/bin/python3
"""
script that lists all states with a name starting with N
takes 3 arguments username, passwd and db name
"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    conn = MySQLdb.connect(name=argv[1], passwd=arg[2], db=argv[3])
    cur = conn.cursor
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'\
            ORDER BY states.id ASC")
    states = cur.fetchall()
    for row in states:
        if row[1][0] == 'N':
            print(row)
    cur.close()
    conn.close()
