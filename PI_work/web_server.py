from flask import Flask
import sqlite3
import random

app=Flask(__name__)

@app.route('/getpin/<pin>')
def index(pin):
    conn=sqlite3.connect(r"information.db")
    c_cursor=conn.cursor()
    ret_value="0"
    for row in c_cursor.execute("select * from keytable"):
        if row[1]==pin:
            c_cursor.execute("update info set flag=1 where aadhaar=?",(row[2],)) 
            c_cursor.execute("delete from keytable where aadhaar=?",(row[2],))
            rand_num=(random.randint(0,9))+(10*(random.randint(0,9)))+(100*(random.randint(0,9)))+(1000*(random.randint(0,9)))
            c_cursor.execute("insert into votekey(id,key) values (?,?)",(None,rand_num))
            ret_value="1"+str(rand_num)
            conn.commit()
            break
    c_cursor.close()
    conn.close()        
    return ret_value

@app.route('/getvote/<vote>')
def voteindex(vote):
    """ Value= Key + Vote"""
    conn=sqlite3.connect(r"information.db")
    c_cursor=conn.cursor()
    ret_value="False"
    for row in c_cursor.execute("select * from votekey"):
        if int(str(vote)[:4])==row[1]:
            c_cursor.execute("update votetable set votecount=votecount+1 where id=?",(vote[4:],))
            c_cursor.execute("delete from votekey where key=?",(row[1],))
            conn.commit()
            ret_value="True"
            break
    
    c_cursor.close()
    conn.close()
    return ret_value

if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0")