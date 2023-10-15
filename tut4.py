import cv2
cap=cv2.VideoCapture(0);
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
cap.set(4,2000)
cap.set(3,10000)
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
while (cap.isOpened()):
    res,frame=cap.read()
    if res==True:
        cv2.imshow("frame",frame)
        if cv2.waitKey(1) & 0xFF==ord('q'):
             break
    else:
          break
cap.release()
cv2.destroyAllWindows()