#!/usr/bin/python3
"""
script lists all state from db hbtn_0e_usa
takes 3 args mysql username, mysql passwd, db name
"""


if __name__ = "__main__":
    from sys import argv
    import MySQLdb
    conn = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states ORDER BY states.id ASC""")
    state_li = cur.fetchall()
    for row in state_li:
        print(state)
    cur.close()
    conn.close()
