import face_recognition
import cv2

for i in range(1, 6):
    # Load an image
    image = face_recognition.load_image_file(f"images/img{i}.jpg")

    # Convert the image from RGB to BGR (since OpenCV uses BGR)
    image_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Find all the faces in the image
    face_locations = face_recognition.face_locations(image)

    # Create a named window and resize it
    cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("Image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    # Draw a rectangle around each face
    for (top, right, bottom, left) in face_locations:
        # The arguments are: the image, top-left coordinates, bottom-right coordinates, border color, border thickness
        cv2.rectangle(image_bgr, (left, top), (right, bottom), (0, 255, 0), 2)

    # Display the image
    cv2.imshow("Image", image_bgr)
    cv2.waitKey(0)  # Waits until a key is pressed
    cv2.destroyAllWindows()  # Closes the window

    # Now face_locations is a list of tuples where each tuple contains the coordinates of a face in the image
    print("I found {} face(s) in this photograph.".format(len(face_locations)))
