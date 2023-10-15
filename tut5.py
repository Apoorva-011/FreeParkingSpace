import cv2
import datetime
cap=cv2.VideoCapture(0);
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#cap.set(4,2000)
#cap.set(3,10000)
#print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
while (cap.isOpened()):
    res,frame=cap.read()
    if res==True:
        font=cv2.FONT_HERSHEY_COMPLEX
        text="width"+str(cap.get(3))+"height:"+str(cap.get(4))
        datet=str(datetime.datetime.now())
        frame=cv2.putText(frame,datet,(10,50),font,2,(0,255,0),2,cv2.LINE_AA)
        cv2.imshow("frame",frame)
        if cv2.waitKey(1) & 0xFF==ord('q'):
             break
    else:
          break
cap.release()
cv2.destroyAllWindows()