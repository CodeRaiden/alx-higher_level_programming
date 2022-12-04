#!/usr/bin/python3
"""
script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches
the argument.
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    conn = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}'\
    ORDER BY states.id in ASC".format(argv[4]))
    sts = cur.fetchall()
    for row in sts:
        if row[1] == argv[4]:
            print(row)
    cur.close()
    conn.close()
