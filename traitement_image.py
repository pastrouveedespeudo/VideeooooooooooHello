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



class traitement_image:
    
 
    def recup_couleur(self):

        os.chdir(r"C:\Users\jeanbaptiste\video\tronche_coul")
        liste = os.listdir()

        self.im = cv2.imread(liste[-1])
        self.im.shape[0]
        self.im.shape[1]
        #ou -2
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
        
        

        for x in range(self.im.shape[0]):
            for y in range(self.im.shape[1]):
            
            if im[x,y][0] != self.liste_couleur[0][0][0] and im[x,y][1] != self.liste_couleur[0][0][1] and im[x,y][2] != self.liste_couleur[0][0][2] and\
               im[x,y][0] != self.liste_couleur[1][0][0] and im[x,y][1] != self.liste_couleur[1][0][1] and im[x,y][2] != self.liste_couleur[1][0][2] and\
               im[x,y][0] != self.liste_couleur[2][0][0] and im[x,y][1] != self.liste_couleur[2][0][1] and im[x,y][2] != self.liste_couleur[2][0][2] and\
               im[x,y][0] != self.liste_couleur[3][0][0] and im[x,y][1] != self.liste_couleur[3][0][1] and im[x,y][2] != self.liste_couleur[3][0][2] and\
               im[x,y][0] != self.liste_couleur[4][0][0] and im[x,y][1] != self.liste_couleur[4][0][1] and im[x,y][2] != self.liste_couleur[4][0][2] and\
               im[x,y][0] != self.liste_couleur[5][0][0] and im[x,y][1] != self.liste_couleur[5][0][1] and im[x,y][2] != self.liste_couleur[5][0][2] and\
               im[x,y][0] != self.liste_couleur[6][0][0] and im[x,y][1] != self.liste_couleur[6][0][1] and im[x,y][2] != self.liste_couleur[6][0][2] and\
               im[x,y][0] != self.liste_couleur[7][0][0] and im[x,y][1] != self.liste_couleur[7][0][1] and im[x,y][2] != self.liste_couleur[7][0][2] and\
               im[x,y][0] != self.liste_couleur[8][0][0] and im[x,y][1] != self.liste_couleur[8][0][1] and im[x,y][2] != self.liste_couleur[8][0][2] and\
               im[x,y][0] != self.liste_couleur[9][0][0] and im[x,y][1] != self.liste_couleur[9][0][1] and im[x,y][2] != self.liste_couleur[9][0][2] and\
               im[x,y][0] != self.liste_couleur[10][0][0] and im[x,y][1] != self.liste_couleur[10][0][1] and im[x,y][2] != self.liste_couleur[10][0][2] and\
               im[x,y][0] != self.liste_couleur[11][0][0] and im[x,y][1] != self.liste_couleur[11][0][1] and im[x,y][2] != self.liste_couleur[11][0][2] and\
               im[x,y][0] != self.liste_couleur[12][0][0] and im[x,y][1] != self.liste_couleur[12][0][1] and im[x,y][2] != self.liste_couleur[12][0][2] and\
               im[x,y][0] != self.liste_couleur[13][0][0] and im[x,y][1] != self.liste_couleur[13][0][1] and im[x,y][2] != self.liste_couleur[13][0][2] and\
               im[x,y][0] != self.liste_couleur[14][0][0] and im[x,y][1] != self.liste_couleur[14][0][1] and im[x,y][2] != self.liste_couleur[14][0][2] and\
               im[x,y][0] != self.liste_couleur[15][0][0] and im[x,y][1] != self.liste_couleur[15][0][1] and im[x,y][2] != self.liste_couleur[15][0][2]:
               
               
                im[x,y] = [0,0,0]
            



    def contour1(self):
        
        imgray = cv2.cvtColor(self.im, cv2.COLOR_BGR2GRAY)
        ret,thresh = cv2.threshold(imgray,127,255,0)
        img2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours (self.im, contours, -1, (0,255,0), 20)


    def nettoyage(self):

        for x in range(self.im.shape[0]):
            for y in range(self.im.shape[1]):
                if self.im[x,y][0] != 0 and self.im[x,y][1] != 255 and self.im[x,y][2] != 0:
                    self.im[x,y] = [0,0,0]



    def countour2(self):
 
        im = array(Image.open(self.im).convert('L'))

        # create a new figure
        figure()

        # show contours with origin upper left corner
        contour(im, origin='image')
        axis('equal')

        im.save("extraction.png",im)

        


                
