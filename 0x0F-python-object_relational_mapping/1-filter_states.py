#!/usr/bin/python3
"""
Script to list all states with a name starting with 'N'
should take 3 arguments username, passwd and db name
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    conn = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states where name LIKE 'N%'\
                 ORDER BY states.id ASC")
    states = cur.fetchall()
    for row in states:
        if row[1][0] == 'N':
            print(row)
    cur.close()
    conn.close()
