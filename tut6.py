import cv2
import numpy as np
#events=[i for i in dir(cv2) if 'EVENT' in i]
#print(events)
def click_event(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        print(x,y)
        font=cv2.FONT_HERSHEY_COMPLEX
        str2=str(x)+','+str(y)
        cv2.putText(img,str2,(x,y),font,1,(255,255,0),3)
        cv2.imshow('img',img)
    if event==cv2.EVENT_RBUTTONDOWN:
       blue=img[y,x,0]
       green=img[y,x,1]
       red=img[y,x,2]
       font=cv2.FONT_HERSHEY_COMPLEX
       str1=str(blue)+','+str(green)+','+str(red)
       cv2.putText(img,str1,(x,y),font,1,(0,255,255),3)
       cv2.imshow('img',img)
img=cv2.imread('lena.jpg')
cv2.imshow('img',img)
cv2.setMouseCallback('img',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()

