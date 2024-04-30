#opencv ka kaam prolly image processing and face recognition ky lie hota ha
import cv2

# video_cap = cv2.VideoCapture(0)  # <-- to on camera and enable video useing variable

# while True:   #<--- camera  ko permantly on krna h 
#     ret , video = video_cap.read()   #<--- to read images use two variable ret , video and .read()
#     cv2.imshow('video live', video)  #<--- imshow is used to create a frmae for it 
#     if cv2.waitKey(10) == ord("a"):  #<-- if i press a it must exit it waitkey paticular time period ky lie stop hoskti h
#         break
# video_cap.release() #<--- to relase video_cap use.realse()


# for facedetection-----------------

face_cap = cv2.CascadeClassifier("C:/Users/Meesam/AppData/Local/Programs/Python/Python312/Lib/site-packages/cv2/datahaarcascade_frontalface_default.xml") #<---  face ky classes ko capture krny ky lie  use this(eyes nose etc)
video_cap = cv2.VideoCapture(0)  
while True:   
    ret , video = video_cap.read()  
    # face ky around box show krwana h for that we have to switch to black and white 
    color = cv2.cvtColor(video , cv2.COLOR_BAYER_BG2GRAY) #<--- jo images ayien hein usko change krna
    faces = face_cap.detectMultiScale(   #<--- use for face structure
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30),
        flags= cv2.CASCADE_SCALE_IMAGE
    )
    for(x , y ,w,h)in faces:
        cv2.rectangle(video,(x+y),(x+w,y+h),(0,255,0),2)
        
    cv2.imshow('video live', video)   
    if cv2.waitKey(10) == ord("a"):  
        break
video_cap.release() 