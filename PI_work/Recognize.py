import face_recognition
picture_of_me = face_recognition.load_image_file("me.jpg")
my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

picture_of_you = face_recognition.load_image_file("me2.jpg")
your_face_encoding = face_recognition.face_encodings(picture_of_you)[0]
    

results = face_recognition.compare_faces([my_face_encoding],your_face_encoding )
if results[0] == True:
    print("It's a picture of me!")
    
