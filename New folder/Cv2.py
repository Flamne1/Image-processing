import cv2

faceCasecade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default')

def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    features=classifier.detectMultiScale(gray,scaleFactor,minNeighbors)
    coords=[]
    for (x,y,w,h) in features :
        cv2.rectangle (img,(x,y),(x+w,y+h), color,2 )
        cv2.putText(img,text,(x,y-4),cv2.FONT_HERSHEY_SIMPLEX,0.8,color,1)
    return img 
def detect(img,faceCasecade):
    img=draw_boundary(img,faceCasecade,1.1,10,(0,0,255),"Face of Human So Handsome")
    return img


cap = cv2.VideoCapture(0)
while (True):
    ret, frame = cap.read()
    frame=detect(frame,faceCasecade)
    cv2.imshow('frame',frame)
    if(cv2.waitKey(1) & 0xFF == ord ('q')):
        break
    
cap.release()
cv2.destroyAllWindows()
