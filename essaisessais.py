from PIL import ImageGrab
from PIL import *
from PIL import Image
from outils_image import *
import time
import shutil
import os
from numpy import *
from cv2 import *
import matplotlib.pyplot as plt
import random
from statistics import mean



face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


img = cv2.imread("10020_5.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]



    #crop = img[y:h+y, x:w+x]
    #cv2.imshow("yooo.png", crop)
    cv2.imshow("yooo.png", img)




im = Image.open("10020_5.png")
pix = im.load()

b = pix[100,200]

listeR = []
listeV = []
listeB = []


for i in range(20):
    pixx = random.randint(0,im.size[0] -1)
    pixy = random.randint(0,im.size[1] - 1)
    a = pix[pixx,pixy]

    listeR.append(a[0])
    listeV.append(a[1])
    listeB.append(a[2])


okR = 0
okV = 0
okB = 0


c = 0

while ok != True
    
    for i in listeR:
        try:
            if listeR[c+1] =< listeR[c] + 30 and listeR[c] >= listeR[c] - 30:
                okR +=1
        except:
            pass
        finally:
            if okR == len(listeR):
                break
           
    for i in listeV:
        try:
            elif listeV[c+1] =< listeV[c] + 30 and listeV[c] >= listeV[c] - 30:
                okV +=1
        except:
            pass
        finally:
            if okV == len(listeV):
                break

   
    for i in listeB:
        try:
            elif listeB[c+1] =< listeB[c] + 30 and listeB[c] >= listeB[c] - 30:
                okB +=1
        except:
            pass
        finally:
            if okB == len(listeB):
                break
    okR = 0
    okV = 0
    okB = 0



MB = mean(listeB)        
  
MV= mean(listeV)

MR = mean(listeR)


print(b)
print(MR)
print(MV)
print(MB)




#print(b,c,d)




"""
x = 0
y = 0

liste = []

while True:
    
    img = pix[x,y]
    x+=1
    if x == im.width  - 1:
        y+=1
        x=0
        
    elif y == im.height - 1:
        break
    
    if img[0] >= b - 30 or img[0] <= b + 30:
        liste.append((x,y))

    elif img[1] >= c - 30 or img[1] <= cb + 30:
        liste.append((x,y))

    elif img[2] >= d - 30 or img[2] <= d + 30:
        liste.append((x,y))


    


    
#print(liste)






"""











#c pas bien beau MAIS ca peut marcher ^^








