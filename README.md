# Face-Detection-using-Viola-Jones-Algorithm
This is a Streamlit app that uses the Viola-Jones algorithm to detect faces from a webcam video stream. The app is written in Python and uses the OpenCV library for image processing.

# Usage
To use the app, you need to have Python and Streamlit installed on your computer. You can install Streamlit by running the following command in your terminal:
pip install streamlit.

Then, you can run the app by executing the following command in the terminal:
streamlit run app.py

Once the app is running, you can press the "Detect Faces" button to start detecting faces from your webcam. The app will display the video stream with the detected faces in a pop-up window. You can close the program by pressing the 'q' or 'x' key in the pop-up window.

# Files
The app consists of the following files:

app.py: This is the main Python file that contains the Streamlit app code.

haarcascade_frontalface_default.xml: This is the pre-trained face cascade classifier file that is used by the Viola-Jones algorithm to detect faces.

README.md: This is the file you are reading right now.

# Dependencies
The app uses the following Python libraries:

OpenCV: For image processing and face detection.

Streamlit: For building the web app.

You can install the required dependencies by running the following command in your terminal: pip install opencv-python streamlit
