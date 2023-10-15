import cv2
cap=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc('X','V','I','D')
out=cv2.VideoWriter("dscc",fourcc,20,(670,670))
while (cap.isOpened()):
  res,frame=cap.read()
  if res==True:
         out.write(frame)
         cv2.imshow("frame",frame) 
  if cv2.waitKey(1) & 0xFF==ord('q'):
            break
cap.release()
out.release()
cv2.destroyAllWindows()