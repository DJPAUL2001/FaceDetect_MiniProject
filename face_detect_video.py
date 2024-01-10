import cv2, os
import face_recognition

# Load all known faces
known_faces = {}
for filename in os.listdir("known_faces"):
   image = face_recognition.load_image_file(os.path.join("known_faces", filename))
   encoding = face_recognition.face_encodings(image)[0]
   known_faces[filename.split(".")[0]] = encoding

# Get a reference to the webcam
video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not video_capture.isOpened():
   print("Cannot open camera")
   exit(1)

while True:
  # Grab a single frame of video
  ret, frame = video_capture.read()

  # Quit when the user hits 'q' or the video ends
  if not ret or cv2.waitKey(1) & 0xFF == ord('q'):
      break

  # Find all the faces in the current frame of video
  face_locations = face_recognition.face_locations(frame)
  face_encodings = face_recognition.face_encodings(frame, face_locations)

  # Compare faces with known faces
  for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
      matches = face_recognition.compare_faces(list(known_faces.values()), face_encoding, tolerance=0.5)
      name = "Unknown"

      if True in matches:
          first_match_index = matches.index(True)
          name = list(known_faces.keys())[first_match_index]

      # Draw a box around the face
      cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

      # Draw a label with a name below the face
      cv2.putText(frame, name, (left, bottom + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

  # Display the resulting image
  cv2.imshow('Video', frame)

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
