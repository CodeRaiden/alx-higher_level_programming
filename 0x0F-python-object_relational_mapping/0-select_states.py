#!/usr/bin/python3
"""
script lists all states from db hbtn_0e_0_usa
takes 3 args mysql username, mysql password
database name
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    conn = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states ORDER BY states.id ASC""")
    states = cur.fetchall()
    for row in states:
        print(row)
    cur.close()
    conn.close()
