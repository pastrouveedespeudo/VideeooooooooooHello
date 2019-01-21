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
for value in im.getdata(): # pas très joli mais compréhensible
    if value in dico.keys():
         dico[value] += 1
    else:
         dico[value] = 1



liste_dico = []


for i in dico.values():
    liste_dico.append(i)



liste_dico= sorted(liste_dico, reverse = True)

c = 0
for i in liste_dico:
    print(i)
    print([c for c,v in dico.items() if v==i])
    if c == 30:
        break
    c+=1

   

#ok de gros progres a faire pour les dico wouaw... j'ai rien compris
#ok les lsites compréhension les maths
#jsp qu'a la silli ils vont vite trouvé comment nous rendre immortel pcque la...

#jviens de comprendre les profs avec leur de gros progres a faire merde
#jme rendais pas compte 

im = Image.open("10025_1.png")































