# Door-Access-System-based-on-Facial-Recognition
Uses Machine Learning concepts of Facial Recognition to unlock a door, Contains Face and Eye Detection, Face Storing with Security Additions (OTP SMS request, WhatsApp request), Face training, Face Recognition, Timed-Face Recognition (The recognition window is accessed for 15 seconds) and also Application project of Theft Detection (Timed Scanning  of Entry and Exit, if person doesn't exit within certain time door gets locked). Consists of Admin, Client Interface, WhatsApp Messaging.

### Prerequisites
* Python 3.6 or above
* opencv-python and opencv-contrib-python 
* numpy
* selenium
* twilio
* os
* sys
* DateTime
* Pillow
* time
* threading
* random

### Installing

* Install all the above mentioned modules in PyCharm from 
File-->Settings-->Python Interpreter-->'+'-->(Type the required Modules).
* Paste all the files in the folder where the project is created.
* Create an empty Folder named **"Dataset_Faces"** in the same directory where the python scripts are 
* Create an empty folder called **Trainer** In same directory
* Run the Files in order 
* utilities --> facestoring --> UserRun_FaceStoring (End file for face storing uses utilities and facestoring) --> face training --> facerecognition --> timed_face_recognition --> Application1 (Final File)
