﻿# Face-Recoginition-Model
- This model is based on the Python which is using inbuilt laptop camera with default value (0), if you are using external camera then use the value (1).
- In this code I have used these liblaries cv2, os pickle, face_recognition, numpy, winsound, datetime, firebase_admin, firebase_admin credentials, firebase_admin db.




- #  Introduction to each library

1. **cv2 (OpenCV)**  
   - OpenCV is a powerful library for computer vision and image processing. It provides tools for image manipulation, video capture, face detection, and much more.  

2. **os**  
   - The `os` module in Python provides functions to interact with the operating system, such as file and directory management, environment variables, and process control.  

3. **pickle**  
   - The `pickle` module is used to serialize and deserialize Python objects, allowing data to be saved to a file or transferred across systems.  

4. **face_recognition**  
   - A specialized library built on top of `dlib`, it enables easy implementation of face detection, face recognition, and face encoding using machine learning models.  

5. **numpy**  
   - NumPy is a foundational library for numerical computations in Python, offering support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions.  

6. **winsound**  
   - A Windows-specific module for generating sound events, such as beeps, using the system speaker. It’s often used for alerts or notifications.  

7. **datetime**  
   - The `datetime` module allows you to work with dates and times, providing tools to parse, manipulate, and format date-time objects.  

8. **firebase_admin**  
   - Firebase Admin SDK is used to interact with Firebase services, such as authentication, Firestore, real-time databases, and cloud messaging, programmatically.  

9. **credentials** (from firebase_admin)  
   - This module helps authenticate access to Firebase services by using credentials, typically in the form of service account keys.  

10. **db (from firebase_admin)**  
    - Provides access to Firebase Realtime Database, enabling you to read and write structured data in real-time applications.  




# Small Changes to focus on after cloning

1. Remember to give a correct file location of **.json** file which will be downloaded from the Google Firebase admin page.
2. To give a correct databaseURL which you will be get from Google Firebase ubder the Realtime database Option.
3. Replace the default image with your images with Unique ID.
4. Last but not the list remember to give a correct file location where so ever necessary





# Code Run
First of all run the EncodeGenerator.py to encode the face data and into 128 dimensional value into 6 vector value.......
Then run AddDataToDatabase.py
Then at last you have to run main.py code to successfully scan the image's and get the output in the terminal.🟢
