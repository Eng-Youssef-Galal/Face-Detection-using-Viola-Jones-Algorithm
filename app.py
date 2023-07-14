import cv2
import streamlit as st


face_cascade = cv2.CascadeClassifier('C:/Users/userH/Desktop/facial recognition project/haarcascade_frontalface_default.xml')


def detect_faces():
    # Initialize webcam
    cap = cv2.VideoCapture(0)
   
    # Load face cascade classifier
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
   
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
       
        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       
        # Detect faces in the grayscale frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
       
        # Draw rectangles around detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
       
        # Display the resulting frame
        cv2.imshow('frame', frame)
       
        # Exit loop and release resources when 'q' key is pressed
        key = cv2.waitKey(1)
        if key == ord('q') or key == ord('x'):
            break
   
    # Release webcam and all windows
    cap.release()
    cv2.destroyAllWindows()


def app():
    st.title("Face Detection using Viola-Jones Algorithm")
    st.write("Press the button below to start detecting faces from your webcam")
    # Add a button to start detecting faces
    if st.button("Detect Faces"):
        # Call the detect_faces function
        detect_faces()

if __name__ == "__main__":
    app()