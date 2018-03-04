import sqlite3

conn=sqlite3.connect(r"information.db")
c_cursor=conn.cursor()
x=0
for row in c_cursor.execute("select * from votetable"):
    x=x+1
    print(row)
    print()
print (x)
c_cursor.close()
conn.close()