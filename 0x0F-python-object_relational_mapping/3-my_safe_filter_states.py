#!/usr/bin/python3
"""lists all states, safe from MySQL injections!"""


if __name__ == "__main__":

    import sys
    import MySQLdb
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name = \
                %s ORDER BY states.id ASC ", (sys.argv[4],))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
