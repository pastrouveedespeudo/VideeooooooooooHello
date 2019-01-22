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
from operator import itemgetter
from collections import OrderedDict
import numpy as np


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
#print(b)




dico = {}
for value in im.getdata():
    if value in dico.keys():
         dico[value] += 1
    else:
         dico[value] = 1



liste_dico = []
for i in dico.values():
    liste_dico.append(i)
    
liste_dico= sorted(liste_dico, reverse = True)



c = 0
liste_couleur = []
for i in liste_dico:
    liste_couleur.append([c for c,v in dico.items() if v==i])
    if i < 100:
        break

print(liste_couleur)

im = cv2.imread("10020_5.png")

#im[200:300, 50] = [255,255,255]


for x in range(im.shape[0]):
    for y in range(im.shape[1]):

        if im[x,y][0] != 0 and im[x,y][1] != 0 and im[x,y][2] != 0:
            im[x,y] = [0,0,255]
        




            
        

       
    

#apres 100 000 0 00 0 00 tentatives avec du couleur peau avec du noir ca marche ouf

#for j in range(im.shape[1]):
#    print(j)
    
cv2.imshow("jojo.png", im)




        
 























