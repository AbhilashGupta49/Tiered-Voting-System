import sqlite3
conn=sqlite3.connect(r"information.db")
c_cursor=conn.cursor()
create_table = """ CREATE TABLE IF NOT EXISTS votekey (
                                        id integer PRIMARY KEY,
                                        key integer NOT NULL
                                        ); """


c_cursor.execute(create_table)
    
conn.commit()
c_cursor.close()
conn.close()
