from PIL import ImageGrab
from PIL import *
from PIL import Image
import PIL
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
from matplotlib.pyplot import *
import os


LISTE = [(0,0)]

class irl_tete:


            
    def capture_ecran(self, i):

        self.i = i

        self.image = str(self.i) + "irl_0.png"
        self.image1 = str(self.i) + "irl_1.png"
        self.image2 = str(self.i) + "irl_2.png"
        self.image3 = str(self.i) + "irl_3.png"
        self.image4 = str(self.i) + "irl_4.png"
        
        img = ImageGrab.grab()
        self.image = img.save(image)
        

    def crop_tete_irl(self):
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        img = cv2.imread(self.image)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]

            crop = img[y:h+y, x:w+x]
            
        cv2.imwrite(self.image1, img)


    def recup_couleur(self):

        self.im = Image.open(self.image1)
        self.im.size[0]
        self.im.size[1]
        #ou -2
        dico = {}
        for value in self.im.getdata():
            if value in dico.keys():
                 dico[value] += 1
            else:
                 dico[value] = 1


        liste_dico = []
        for i in dico.values():
            liste_dico.append(i)
            
        liste_dico= sorted(liste_dico, reverse = True)


        c = 0
        self.liste_couleur = []

        for i in liste_dico:
            if [c for c,v in dico.items() if v==i] == [(0, 0, 255)]:
                c-=1
            elif [c for c,v in dico.items() if v==i] != [(0, 0, 255)]:
                self.liste_couleur.append([c for c,v in dico.items() if v==i])
            c+=1
            if c == 16:
                break


    def recupe_peau(self):
        
        self.im = cv2.imread(self.image1)
        
        for x in range(self.im.shape[0]):
            for y in range(self.im.shape[1]):
            
                if self.im[x,y][0] != self.liste_couleur[0][0][0] and self.im[x,y][1] != self.liste_couleur[0][0][1] and self.im[x,y][2] != self.liste_couleur[0][0][2] and\
                  self.im[x,y][0] != self.liste_couleur[1][0][0] and self.im[x,y][1] != self.liste_couleur[1][0][1] and self.im[x,y][2] != self.liste_couleur[1][0][2] and\
                   self.im[x,y][0] != self.liste_couleur[2][0][0] and self.im[x,y][1] != self.liste_couleur[2][0][1] and self.im[x,y][2] != self.liste_couleur[2][0][2] and\
                   self.im[x,y][0] != self.liste_couleur[3][0][0] and self.im[x,y][1] != self.liste_couleur[3][0][1] and self.im[x,y][2] != self.liste_couleur[3][0][2] and\
                   self.im[x,y][0] != self.liste_couleur[4][0][0] and self.im[x,y][1] != self.liste_couleur[4][0][1] and self.im[x,y][2] != self.liste_couleur[4][0][2] and\
                   self.im[x,y][0] != self.liste_couleur[5][0][0] and self.im[x,y][1] != self.liste_couleur[5][0][1] and self.im[x,y][2] != self.liste_couleur[5][0][2] and\
                   self.im[x,y][0] != self.liste_couleur[6][0][0] and self.im[x,y][1] != self.liste_couleur[6][0][1] and self.im[x,y][2] != self.liste_couleur[6][0][2] and\
                   self.im[x,y][0] != self.liste_couleur[7][0][0] and self.im[x,y][1] != self.liste_couleur[7][0][1] and self.im[x,y][2] != self.liste_couleur[7][0][2] and\
                   self.im[x,y][0] != self.liste_couleur[8][0][0] and self.im[x,y][1] != self.liste_couleur[8][0][1] and self.im[x,y][2] != self.liste_couleur[8][0][2] and\
                   self.im[x,y][0] != self.liste_couleur[9][0][0] and self.im[x,y][1] != self.liste_couleur[9][0][1] and self.im[x,y][2] != self.liste_couleur[9][0][2] and\
                   self.im[x,y][0] != self.liste_couleur[10][0][0] and self.im[x,y][1] != self.liste_couleur[10][0][1] and self.im[x,y][2] != self.liste_couleur[10][0][2] and\
                   self.im[x,y][0] != self.liste_couleur[11][0][0] and self.im[x,y][1] != self.liste_couleur[11][0][1] and self.im[x,y][2] != self.liste_couleur[11][0][2] and\
                   self.im[x,y][0] != self.liste_couleur[12][0][0] and self.im[x,y][1] != self.liste_couleur[12][0][1] and self.im[x,y][2] != self.liste_couleur[12][0][2] and\
                   self.im[x,y][0] != self.liste_couleur[13][0][0] and self.im[x,y][1] != self.liste_couleur[13][0][1] and self.im[x,y][2] != self.liste_couleur[13][0][2] and\
                   self.im[x,y][0] != self.liste_couleur[14][0][0] and self.im[x,y][1] != self.liste_couleur[14][0][1] and self.im[x,y][2] != self.liste_couleur[14][0][2] and\
                   self.im[x,y][0] != self.liste_couleur[15][0][0] and self.im[x,y][1] != self.liste_couleur[15][0][1] and self.im[x,y][2] != self.liste_couleur[15][0][2]:
                   
                   
                    self.im[x,y] = [0,0,0]
        cv2.imwrite(self.image2, self.im)               

    def contour1(self):
        
        self.im = cv2.imread(self.image2)
        imgray = cv2.cvtColor(self.im, cv2.COLOR_BGR2GRAY)
        ret,thresh = cv2.threshold(imgray,127,255,0)
        img2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours (self.im, contours, -1, (0,255,0), 20)


        cv2.imwrite(self.image3, self.im)

    def nettoyage(self):

        self.im = cv2.imread(self.image3)
        for x in range(self.im.shape[0]):
            for y in range(self.im.shape[1]):
                if self.im[x,y][0] != 0 and self.im[x,y][1] != 255 and self.im[x,y][2] != 0:
                    self.im[x,y] = [0,0,0]
                    
        cv2.imwrite(self.image4, self.im)


    def countour2(self):

        im = array(Image.open(self.image4).convert('L'))

        # create a new figure
        figure()

        # show contours with origin upper left corner
        contour(im, origin='image')
        axis('equal')

        plt.show()
        cv2.imwrite(self.image5, im)



    def pts(self):
 
        img = cv2.imread(self.image5)

        y = 0
        x = 50
    
        liste = []
        while True:
            try:
                if img[x,y][0] != 0 and img[x,y][1] != 0 and img[x,y][2] != 0:
                    liste.append(y)

                y +=1
            except:
                break
            
        liste.sort()
        a = liste[0]
        b = liste[-1]

        LISTE.append((a,b))


    def gauche_ou_droite(self):

        if LISTE[0][0] > LISTE[1][0] + 5:
            print("tete a droite")
        elif LISTE[0][0] < LISTE[1][0] + 5:
            print("tete a gauche")
        else:
            pass

        
        del LISTE[0]







   

yo = essais()
#yo.essais1()
#yo.recup_couleur()
#yo.recupe_peau()
#yo.contour1()
#yo.nettoyage()
#yo.countour2()
#yo.pts()







































