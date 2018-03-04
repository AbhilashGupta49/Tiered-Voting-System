import sqlite3
conn=sqlite3.connect(r"information.db")
c_cursor=conn.cursor()
create_table = """ CREATE TABLE IF NOT EXISTS votetable (
                                        id integer PRIMARY KEY,
                                        votecount integer NOT NULL
                                        ); """


c_cursor.execute(create_table)
for x in range(0,3):
    c_cursor.execute("insert into votetable(id,votecount) values (?,?)",(None,0))
    
conn.commit()
c_cursor.close()
conn.close()