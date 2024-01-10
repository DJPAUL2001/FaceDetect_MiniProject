import face_recognition

known_image = face_recognition.load_image_file("comparison_images/trump.jpg")
unknown_image = face_recognition.load_image_file("comparison_images/mystery1.jpg")

known_encoding = face_recognition.face_encodings(known_image)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

results = face_recognition.compare_faces([known_encoding], unknown_encoding)

if results[0]:
   print("Same Person!")
else:
   print("Different Person.")
