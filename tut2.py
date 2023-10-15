import cv2
import numpy as np
img=np.zeros([512,512,3],np.uint8)
#img=cv2.imread("lena.jpg",1)
img=cv2.line(img,(0,0),(255,255),(0,0,255),3)
img=cv2.arrowedLine(img,(0,255),(255,255),(255,0,0),3)
img=cv2.rectangle(img,(384,0),(510,128),(62,181,94),-1)
img=cv2.circle(img,(447,63),63,(0,255,0),-1)
font=cv2.FONT_HERSHEY_COMPLEX
img=cv2.putText(img,"Beautiful",(10,500),font,2,(255,255,255),10,cv2.LINE_AA)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()