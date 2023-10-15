import cv2
import numpy as np
def click_event(event,x,y,flags,param):
#  if event==cv2.EVENT_LBUTTONDBLCLK:
    # cv2.circle(img,(x,y),3,(0,255,0),-1,)
    # cv2.imshow('image',img)
    # points.append((x,y))
    # if len(points)>=2:
        # cv2.line(img,points[-1],points[-2],(255,0,0),5)
    # cv2.imshow('img1',img)
 if event==cv2.EVENT_LBUTTONDBLCLK:
    blue=[y,x,0]
    green=[y,x,1]
    red=[y,x,2]
    cv2.circle(img,(x,y),3,(0,255,0),-1)
    imaa=cv2.imread('cat.jpg')
    imaa[:]=[blue,green,red]
    cv2.imshow('colr',imaa) 

img=cv2.imread('lena.jpg')
#img=np.zeros([512,512,8],np.uint8)
cv2.imshow('img1',img)
points =[]
cv2.setMouseCallback('img1',click_event)
cv2.waitKey()
cv2.destroyAllWindows()