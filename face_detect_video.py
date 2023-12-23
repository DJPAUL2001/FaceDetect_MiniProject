import cv2
import face_recognition

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

   # Draw a box around each face
   for (top, right, bottom, left) in face_locations:
       cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

   # Display the resulting image
   cv2.imshow('Video', frame)

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
