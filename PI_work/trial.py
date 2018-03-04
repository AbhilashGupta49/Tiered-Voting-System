import sqlite3
import face_recognition
import json
from numpy import array
import numpy
import random


conn=sqlite3.connect(r"information.db")
c_cursor=conn.cursor()
d_cursor=conn.cursor()

c_cursor.execute("drop table keytable")
c_cursor.execute("update info set tries=0")

conn.commit()


create_table = """ CREATE TABLE IF NOT EXISTS keytable (
                                        id integer PRIMARY KEY,
                                        num text NOT NULL,
                                        aadhaar integer NOT NULL,
                                        created_at TIMESTAMP NOT NULL
                                    ); """
c_cursor.execute(create_table)




def disp_screen(val):
    print(val)
    """
    
    Display 4 Digit Number
    
    """
    
def generate_random(num):
    get_digits=str(num)
    get_digits=get_digits[:4]
    rand_num=(random.randint(0,9))+(10*(random.randint(0,9)))+(100*(random.randint(0,9)))+(1000*(random.randint(0,9)))
    totalnum=str(rand_num)+get_digits
    c_cursor.execute("UPDATE info set tries=tries+1 where aadhaar=?",(num,))
    conn.commit()
    disp_screen(rand_num)
    
    return totalnum
    
def green_light():
    """
    GREEN LIGHT
    
    """

def red_light():
    print("Not You")
    
    """
    RED LIGHT
    """
    
def delete_entry():
    c_cursor.execute("delete from keytable where created_at < DATETIME('NOW','-10 minutes')")
    conn.commit()


"""
Change this to button click
"""
picture_of_me = face_recognition.load_image_file("me.jpg")
my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]
"""
"""

d_cursor.execute("select count(id) from keytable")
count_people=d_cursor.fetchone()
delete_entry()
change_value=0
if(count_people[0]<5):
    for row in c_cursor.execute('SELECT aadhaar,photo,flag,tries FROM info'):
        unknown_face=array(json.loads(row[1]))
        results = face_recognition.compare_faces([my_face_encoding], unknown_face)
        if (results[0] == True) and row[2]==0 and row[3]<3:
            print(row[0])
            for row2 in d_cursor.execute("select aadhaar,num from keytable"):
                if (row[0] == row2[0]):
                    d_cursor.execute("UPDATE info set tries=tries+1 where aadhaar=?",(row2[0],))
                    conn.commit()
                    change_value=1
                    disp_screen(row2[1][:4])
                    green_light()
                    break
        
            if (change_value == 0):
                key=generate_random(row[0])
                c_cursor.execute("INSERT INTO keytable(id,num,aadhaar,created_at) VALUES (?,?,?,CURRENT_TIMESTAMP)",(None,key,row[0]))
                conn.commit()
                green_light()
                break
            else:
                break
        else:
            red_light()
            
            
        

for row in c_cursor.execute("select * from keytable"):
    print(row)

c_cursor.close()
d_cursor.close()
conn.close()
