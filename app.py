"""
##############################################################################
#######                 PROJECT NAME : SELFIE ON SMILE                 #######
##############################################################################
                                Synopsis:
Script activates default camera and open window with live feed. Camera will detect
face and smiles. It will save '.png' files as soon it will detect smile on face.
File name of created png is exact date and time.
Face is highlited with green frame, and smile is with red. 
"""


### imports
import cv2
import datetime

### video capture object
camera = cv2.VideoCapture(0)

### face and smile templates
face_cascade = cv2.CascadeClassifier('templates/haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('templates/haarcascade_smile.xml')

while True:
    ### Original frame
    _, frame = camera.read() 
    ### creating original frame copy
    clear_frame = frame.copy() 
    ### converting into grey scale
    greyscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   
    ### face detection
    face = face_cascade.detectMultiScale(greyscale, 1.3, 5) 
    for x,y,w,h in face:
        cv2.rectangle(frame,(x,y), (x+w,y+h), (0,255,255),2)
        face_roi = frame[y:y+h, x:x+w]
        gray_roi = greyscale[y:y+h, x:x+w]
        ### Smile detection
        smile = smile_cascade.detectMultiScale(gray_roi, 1.3,25)
        for x1,y1,w1,h1 in smile:
            cv2.rectangle(face_roi,(x1,y1), (x1+w1,y1+h1), (0,0,255), 2)
            time_stamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
            file = f'{time_stamp}.png'
            ### save file
            cv2.imwrite(file, clear_frame)

    ### Show live feed from camera            
    cv2.imshow('Live Feed',frame)

    ## if pressed 'q' program will end
    key = cv2.waitKey(1)
    if key==ord('q'):
        break