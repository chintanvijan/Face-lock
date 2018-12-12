# Face-lock
A face recognition desktop app created in python to protect your private files and directories by generating a user's face id.

Dependencies for usage:
  1. Python 3.0 or plus.
  2. face_recognition library from python.org and all its dependencies

Instructions for usage:
 Step 1:
  facelock.py is the GUI for using this app, user needs to first select its face image from desktop, this will generate a file named as 'facepath.txt' , this file 'facepath.txt' needs to be copied at the location where the file that is to be protected is stored.
  
  Step 2:
   After step 1 is over , now user can select file or directory using facelock.py (GUI) that is to be protected. A python file with same name with file extension will be generated at that location , which is used to protect that file, whenever that file is tried to be open, laptop camera will be initiated and current user's image will be compared with file owner's image, and origiinal file will only open on successfull comparison.
   
NOTE:- Only for windows OS users
  
