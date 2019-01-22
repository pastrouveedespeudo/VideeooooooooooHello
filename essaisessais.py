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


dico = {}
for value in im.getdata():
    if value in dico.keys():
         dico[value] += 1
    else:
         dico[value] = 1
print("oui")


liste_dico = []
for i in dico.values():
    liste_dico.append(i)
    
liste_dico= sorted(liste_dico, reverse = True)



c = 0
liste_couleur = []

for i in liste_dico:
    liste_couleur.append([c for c,v in dico.items() if v==i])
    c+=1
    if c == 16:
        break





    


im = cv2.imread("10025_6.png")

#ouille lui on voit qu'il fait de grosse journée ^^
#ouais bah...
#bordel que c moche ^^

for x in range(im.shape[0]):
    for y in range(im.shape[1]):
        
        if im[x,y][0] != liste_couleur[0][0][0] and im[x,y][1] != liste_couleur[0][0][1] and im[x,y][2] != liste_couleur[0][0][2] and\
           im[x,y][0] != liste_couleur[1][0][0] and im[x,y][1] != liste_couleur[1][0][1] and im[x,y][2] != liste_couleur[1][0][2] and\
           im[x,y][0] != liste_couleur[2][0][0] and im[x,y][1] != liste_couleur[2][0][1] and im[x,y][2] != liste_couleur[2][0][2] and\
           im[x,y][0] != liste_couleur[3][0][0] and im[x,y][1] != liste_couleur[3][0][1] and im[x,y][2] != liste_couleur[3][0][2] and\
           im[x,y][0] != liste_couleur[4][0][0] and im[x,y][1] != liste_couleur[4][0][1] and im[x,y][2] != liste_couleur[4][0][2] and\
           im[x,y][0] != liste_couleur[5][0][0] and im[x,y][1] != liste_couleur[5][0][1] and im[x,y][2] != liste_couleur[5][0][2] and\
           im[x,y][0] != liste_couleur[6][0][0] and im[x,y][1] != liste_couleur[6][0][1] and im[x,y][2] != liste_couleur[6][0][2] and\
           im[x,y][0] != liste_couleur[7][0][0] and im[x,y][1] != liste_couleur[7][0][1] and im[x,y][2] != liste_couleur[7][0][2] and\
           im[x,y][0] != liste_couleur[8][0][0] and im[x,y][1] != liste_couleur[8][0][1] and im[x,y][2] != liste_couleur[8][0][2] and\
           im[x,y][0] != liste_couleur[9][0][0] and im[x,y][1] != liste_couleur[9][0][1] and im[x,y][2] != liste_couleur[9][0][2] and\
           im[x,y][0] != liste_couleur[10][0][0] and im[x,y][1] != liste_couleur[10][0][1] and im[x,y][2] != liste_couleur[10][0][2] and\
           im[x,y][0] != liste_couleur[11][0][0] and im[x,y][1] != liste_couleur[11][0][1] and im[x,y][2] != liste_couleur[11][0][2] and\
           im[x,y][0] != liste_couleur[12][0][0] and im[x,y][1] != liste_couleur[12][0][1] and im[x,y][2] != liste_couleur[12][0][2] and\
           im[x,y][0] != liste_couleur[13][0][0] and im[x,y][1] != liste_couleur[13][0][1] and im[x,y][2] != liste_couleur[13][0][2] and\
           im[x,y][0] != liste_couleur[14][0][0] and im[x,y][1] != liste_couleur[14][0][1] and im[x,y][2] != liste_couleur[14][0][2] and\
           im[x,y][0] != liste_couleur[15][0][0] and im[x,y][1] != liste_couleur[15][0][1] and im[x,y][2] != liste_couleur[15][0][2]:
           
           
            im[x,y] = [0,0,0]
        




            
        

       
    



#for j in range(im.shape[1]):
#    print(j)
    
cv2.imshow("jojo.png", im)







def only_tete_sans_cheveux(self):
    img = cv2.imread('[601 126 289 289].png')


    mask = np.zeros(img.shape[:2],np.uint8)

    bgdModel = np.zeros((1,65),np.float64)
    fgdModel = np.zeros((1,65),np.float64)

    rect = (50,50,450,290)
    cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)

    mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
    img = img*mask2[:,:,np.newaxis]

    plt.imshow(img),plt.colorbar(),plt.show()





def countour(self):
    img = cv2.imread("10025_6.png")
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    ret,thresh = cv2.threshold(imgray,127,255,0)
    img2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours (img, contours, -1, (0,255,0), 3)


    cv2.imshow('img',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


#1-extraire le corps
#2-extraire les couleurs de la peau de la tete
#3-faire la fonction
#4-find coutour
#5-apres ben j'en sais rien putin oublie pas t'as le truk pts centré round main faut extraire LA MAIN    
 



















