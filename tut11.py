import cv2
import numpy as np
def nothing(x):
  print(x)
cv2.namedWindow('obj')
cv2.createTrackbar('LH','obj',0,255,nothing)
cv2.createTrackbar('LS','obj',0,255,nothing)
cv2.createTrackbar('LV','obj',0,255,nothing)
cv2.createTrackbar('HH','obj',0,255,nothing)
cv2.createTrackbar('HS','obj',0,255,nothing)
cv2.createTrackbar('HV','obj',0,255,nothing)
while(1):
  img=cv2.imread('Mon.jpg.JPG')
  hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
  lh=cv2.setTrackbarPos('LH','obj')
  ls=cv2.setTrackbarPos('LS','obj')
  lh=cv2.setTrackbarPos('LV','obj')
  uh=cv2.setTrackbarPos('UH','obj')
  us=cv2.setTrackbarPos('US','obj')
  uh=cv2.setTrackbarPos('UV','obj')
  lb=np.array([lh,lh,ls])
  ub=np.array([uh,uh,us])
  mask=cv2.inRange(hsv,lb,ub)
  img1=cv2.bitwise_and(img,img,mask=mask)


  cv2.imshow('obj',img1)
  k=cv2.waitKey(1)
  if (k==27):
    break
cv2.destroyAllWindows()