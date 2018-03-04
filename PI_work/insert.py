import sqlite3
import time
import picamera
import face_recognition
import json


conn=sqlite3.connect(r"information.db")
c=conn.cursor()
"""
c.execute("DROP TABLE info")
"""
create_table = """ CREATE TABLE IF NOT EXISTS info (
                                        aadhaar integer PRIMARY KEY NOT NULL,
                                        photo blob NOT NULL,
                                        flag integer NOT NULL,
                                        tries integer NOT NULL
                                        
                                    ); """



c.execute(create_table)

with conn:
    aadhaar=input("Enter Aadhaar - ")
    
    with picamera.PiCamera() as camera:
        
        camera.resolution = (1080, 720)
        camera.start_preview()
        time.sleep(1)
        camera.capture('photo_capture.jpg')
        
        try:
            picture_of_me = face_recognition.load_image_file("photo_capture.jpg")
            cap_face_encoding = face_recognition.face_encodings(picture_of_me)[0]
            encoded_data=json.dumps(cap_face_encoding.tolist())    
            sql="insert into info(aadhaar,photo,flag,tries) values (?,?,?,?)"
            c.execute(sql,(aadhaar,encoded_data,0,0))
            conn.commit()
        except:
            print("Error in Insertion (Face not detected/DB error)")
            
"""        
      
for row in c.execute('SELECT * FROM info'):
    print (json.loads(row[1]))
"""    
c.close()
conn.close()