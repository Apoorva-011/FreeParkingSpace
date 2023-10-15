import cv2
import numpy as np
img=cv2.imread('lena.jpg')
print(img.shape)
print(img.size)
print(img.dtype)
b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))
paws=img[250:330]
img[10:90]=paws
l=cv2.resize('lena.jpg',(10,10))
c=cv2.resize('cat.jpg',(10,10))
#d=cv2.add(l,c)
e=cv2.addWeighted(l,0.1,c,0.9,0)
cv2.imshow('img',e)
cv2.waitKey(0)
cv2.destroyAllWindows()
