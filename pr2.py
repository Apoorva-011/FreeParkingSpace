import cv2
import pickle
img=cv2.imread('carParkImg.png')
width=107
height=48
posList=[]
try:
  with open('CarParkPos', 'rb') as f:
    posList = pickle.load(f)
except:
    posList=[]

def mouseclick(events,x,y,flags,params):
    if events == cv2.EVENT_LBUTTONDBLCLK:
        posList.append((x,y))
    if events == cv2.EVENT_RBUTTONDBLCLK:
        for i,pos in enumerate(posList):
            x1,y1=pos
            if x1<x<x1+width and y1<y<y1+height:
                posList.pop(i)
  
while True:
    #cv2.rectangle(img,(50,192),(157,240),(255,0,255),2)
    for pos in posList:
        cv2.rectangle(img,pos,(pos[0]+width,pos[1]+height),(255,0,255),2)
    cv2.imshow("img1",img)
    cv2.setMouseCallback("img1",mouseclick)
    cv2.waitKey(10)