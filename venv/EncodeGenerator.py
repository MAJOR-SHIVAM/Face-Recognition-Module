import cv2
import face_recognition
import os
import pickle

# Define the path to the folder containing student images
folderPath = "Images"

# Check if the folder exists
if not os.path.exists(folderPath):
    print(f"Error: The folder '{folderPath}' does not exist.")
else:
    # Get a list of all files in the folder
    pathList = os.listdir(folderPath)
    print("List of image files:", pathList)

    imgList = []
    studentsIds = []

    # Load each image and store it with the associated student ID
    for path in pathList:
        # Read the image and append it to imgList
        img = cv2.imread(os.path.join(folderPath, path))
        if img is None:
            print(f"Warning: Could not read image '{path}'. Skipping.")
            continue

        imgList.append(img)
        # Extract the student ID (file name without extension) and append it to studentsIds
        studentsIds.append(os.path.splitext(path)[0])

    # Print final list of student IDs for debugging
    print("Student IDs:", studentsIds)

    def findEncodings(imagesList):
        encodeList = []
        for img in imagesList:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList

    print("Encoding Started...⏳⌛")
    encodeListKnown = findEncodings(imgList)
    encodingListKnownWithIds = [encodeListKnown, studentsIds]

    # Debug: Print encoding data for verification
    for i, encoding in enumerate(encodeListKnown):
        print(f"Encoding for {studentsIds[i]}: {encoding[:5]}...")  # Print the first 5 values of each encoding for a quick check

    print("Encoding Complete")
    file = open("EncodeFile.p", "wb")
    pickle.dump(encodingListKnownWithIds, file)
    file.close()
    print("File Saved 🟢")
