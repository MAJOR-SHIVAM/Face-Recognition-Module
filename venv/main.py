import cv2
import os
import pickle
import face_recognition
import numpy as np
import winsound
import datetime

from firebase_admin import credentials, db, initialize_app

# Initialize Firebase (ensure path to service account key is correct)
cred = credentials.Certificate("File location of .json file")
initialize_app(cred, {'databaseURL': "Google firebase database URL"})

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

imgBackground = cv2.imread("Resources/background.png")

# Importing mode images into a list
folderModePath = "Resources/Modes"
modePathList = os.listdir(folderModePath)
imgModeList = []

for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))

# Load the encoding file
print("Loading Encoded file...")
file = open("EncodeFile.p", "rb")
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownWithIds
print("Encoded File Loaded Successfully")

modeType = 0
counter = 0
id = -1
previously_scanned_ids = set()

beep_frequency = 1000
beep_duration = 500

while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture image")
        break

    # Resize for faster processing, and convert to RGB
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    # Display the webcam feed on the background
    imgBackground[162:162 + 480, 55:55 + 640] = img
    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]

    for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
        # Compare the face encodings
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

        # Find the best match by minimum distance
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex] and faceDis[matchIndex] < 0.6:  # Typical threshold for face match
            id = studentIds[matchIndex]

            if id not in previously_scanned_ids:  # If the student hasn’t been marked present yet
                # Fetch the current time
                current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"Attendance marked for ID: {id} at {current_time}")  # Print the time to the terminal

                winsound.Beep(beep_frequency, beep_duration)
                previously_scanned_ids.add(id)  # Add the student ID to the set of scanned students
                counter = 1  # Set counter to 1 to indicate attendance has been marked
                modeType = 1  # Switch mode to show the "Attendance Taken" screen

                # **NEW CODE BLOCK**: Load and display the student's photo
                student_image_path = os.path.join("Images", f"{id}.jpg")  # Assuming images are .jpg
                if os.path.exists(student_image_path):
                    student_img = cv2.imread(student_image_path)
                    # Resize and place the photo on the right-hand side
                    student_img_resized = cv2.resize(student_img, (150, 200))  # Adjust size as needed
                    imgBackground[50:250, 900:1050] = student_img_resized  # Adjust coordinates as needed
                else:
                    print(f"Photo for student ID {id} not found!")

            else:  # If the same student appears again (double entry)
                winsound.Beep(1500, 500)  # Play "Double Entry" sound (different frequency and duration)
                counter = 0  # Reset counter to avoid marking attendance again

        if counter != 0:
            if counter == 1:
                studentInfo = db.reference(f'Students/{id}').get()
                print(studentInfo)  # Debug print

                # Draw a rectangle for the information box
                cv2.rectangle(imgBackground, (50, 50), (350, 150), (0, 0, 0), cv2.FILLED)

                cv2.putText(imgBackground, f"Name: {studentInfo['Name']}", (60, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
                cv2.putText(imgBackground, f"ID: {id}", (60, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
                cv2.putText(imgBackground, f"Faculty: {studentInfo['faculty']}", (60, 140), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
                print('\n')

            counter += 1

            # Reset counter after a few frames to allow for continuous checking
            if counter > 10:
                counter = 0
                modeType = 0

    cv2.imshow("Face Attendance System", imgBackground)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
