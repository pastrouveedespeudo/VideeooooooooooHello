import numpy as np
import cv2
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = cv2.imread('poucemec.png')


a = int(round(img.shape[1]/2))
b = int(round(img.shape[0]/2))

x = 0
y = 0
liste = []
while True:

    px = img[x,y]

    if  x == img.shape[0]-1:
        y+=1
        x = 0
    elif y == img.shape[1] -1:
        break


    liste.append(str(x))
    liste.append(str(y))
    liste.append(str(px))
    
    x+=1


liste2 =[]
c = 0
for i in liste:
    try:
        if liste[c+3] == "[255 255 255]":
            
            liste2.append(liste[c+1])
            
        c+=1
   
    except:
        pass



liste3 = []
for i in liste2:
    liste3.append(int(i))



r = int(round(max(liste3)/2))
cv2.circle(img, (a,b), r, (0,0,255),3)





















cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
