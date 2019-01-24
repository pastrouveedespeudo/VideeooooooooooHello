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

LISTE = ["jjo"]
class essais:
    def essais1(self):
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

  
        img = cv2.imread("coucou.png")

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]

            crop = img[y:h+y, x:w+x]
            
        cv2.imshow("fer.png", img)
        cv2.imwrite("yoyo.png", img)

   

 
 
    def recup_couleur(self):

        self.im = Image.open("coucou.png")
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


        print(self.liste_couleur)

   
    def recupe_peau(self):
        
        self.im = cv2.imread("coucou.png")
        
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
        cv2.imwrite("coucou1.png", self.im)               

    def contour1(self):
        
        self.im = cv2.imread("coucou1.png")
        imgray = cv2.cvtColor(self.im, cv2.COLOR_BGR2GRAY)
        ret,thresh = cv2.threshold(imgray,127,255,0)
        img2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours (self.im, contours, -1, (0,255,0), 20)


        cv2.imwrite("coucou2.png", self.im)

    def nettoyage(self):

        self.im = cv2.imread("coucou2.png")
        for x in range(self.im.shape[0]):
            for y in range(self.im.shape[1]):
                if self.im[x,y][0] != 0 and self.im[x,y][1] != 255 and self.im[x,y][2] != 0:
                    self.im[x,y] = [0,0,0]
                    
        cv2.imwrite("coucou3.png", self.im)


    def countour2(self):

        im = array(Image.open('coucou3.png').convert('L'))

        # create a new figure
        figure()

        # show contours with origin upper left corner
        contour(im, origin='image')
        axis('equal')

        plt.show()
        cv2.imwrite("coucou4.png", im)



    def pts(self):
 
        img = cv2.imread("coucou4.png")

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

        
        #print(a,b)
        #img[50,37:278] = [0,0,255]

        #mtn si la 2eme est plus grande alors ca penche a gauche
        #plus petite a droite
        #il faut faire une diff minimum
        #s'il baisse la tete alors x et y auront tous les deux du trait

        #OU
        #y'a du noir depuis a et du blanc a b -> gauche
        #

        
        cv2.imshow("yaya.png", img)

yo = essais()
#yo.essais1()
#yo.recup_couleur()
#yo.recupe_peau()
#yo.contour1()
#yo.nettoyage()
#yo.countour2()
yo.pts()







































