import cv2 as cv
 

def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
   return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)


capture =cv.VideoCapture('video/sample-5s.mp4')
while True:
  isTrue ,frame =capture.read()
  frameres= rescaleFrame(frame)
  cv.imshow('vieww',frame)
  cv.imshow('resized',frameres)
 
 if cv.waitKey(20):
     break