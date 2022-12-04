#!/usr/bin/python3
"""
script lists all states from db hbtn_0e_0_usa
takes 3 args mysql username, mysql password
database name
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    conn = MySQLdb.connect(username=argv[1], password=argv[2], database=argv[3])
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states ORDER BY states.id ASC""")
    state_li = cur.fetchall()
    for row in state_li:
        print(row)
    cur.close()
    conn.close()
