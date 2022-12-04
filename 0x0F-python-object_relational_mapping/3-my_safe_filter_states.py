#!/usr/bin/python3
"""
script that is safe from SQL injections
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    conn = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    check = (argv[4], )
    cur.execute("SELECT * FROM states WHERE name = '{}'\
    ORDER BY states.id ASC".format(check))
    sts = cur.fetchall()
    for row in sts:
        print(row)
    cur.close()
    conn.close()
