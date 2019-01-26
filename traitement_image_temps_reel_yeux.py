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
import threading
import time
from PIL import Image
from pylab import *

class irl_yeux:

    def position_yeux(self):

        self.i = 0
        self.name = str(self.i) + "yeux.png"
        self.name1 = str(self.i) + "_2yeux.png"
        self.name = str(self.i) + "_yeux.png"
        self.name = str(self.i) + "_yeux.png"
        self.name = str(self.i) + "_yeux.png"
        self.name = str(self.i) + "_yeux.png"
        
        eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        
        img = cv2.imread('femme.jpg')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)

            crop = img[y:h+y, x:w+x]
            
     
            for (ex,ey,ew,eh) in eyes:

                cv2.rectangle(roi_color, (ex,ey),(ex+ew,ey+eh),(0,0,255),2)               
                crop1 = roi_color[ey:ey+eh, ex:ex+ew]
                
            
                crop2 = roi_color[ey+10:ey+eh-10, ex:ex+ew]

        cv2.imshow("tt.png", crop2)
        cv2.imwrite("tt.png", crop2)
        cv2.imwrite("yoy.png", crop)
        cv2.imwrite("yy.png", crop1)



    def transforme_image(self):
        
        
        image_pts = cv2.imread("yoy.png", 0)
        edges = cv2.Canny(image_pts,100,200)
        plt.subplot(122),plt.imshow(edges,cmap = 'gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
        cv2.imwrite("yoyo.png", image_pts)
        cv2.imshow("ezeza", image_pts)





        
    def yeux(self):

  
        im = cv2.imread("tt.png")
        for x in range(im.shape[0]):
            for y in range(im.shape[1]):
             

                if im[x,y][0] == 255 or im[x,y][0] >= 150 and im[x,y][1] == 255 or\
                   im[x,y][1] >= 150 and im[x,y][1] == 255 or im[x,y][2] >= 150:
                    pass
                else:
                    im[x,y] = [255,255,255]
        cv2.imshow("couocu.png", im)
        cv2.imwrite("couocu.png", im)

        im = cv2.imread("couocu.png")
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

        
        


    def contour(self):
        
        im = array(Image.open('couocu.png').convert('L'))

        figure()
        
        contour(im, levels=[245], colors='black', origin='image')
        axis('equal')

        
        show()
       


    def geometrie(self):
        pass
        #carre = {cid:(x,y), td:(x, x:nombrex), tdh:(nombrex:y +nombrey), tdy:(nombrex,nombrey-nombrex)}
        #hexagone ={1: (x,y),
         #          2:(x,(x:nombrex)),
         #          3:((x:nombrex+1/2*nombrex,y:1/2*nombrey)),
         #          4:((x+nombrex+1/2*nombrex,y:1/2*nombrey+nombrey))
         #          5:((x:nombrex, y+2*nombrey)),
          #         6:((x, y:2*nombrey)),
          #         7:((x:-1/2*nombrex, 2*nombrey:2*nombrey - 1/2*nombrey))
         #          8:((-1/2*nombrex, 2*nombrey - 1/2*nombrey - nombrey))
          #         9:((-1/2*nombrex:x, 1/2*nombrey:y))
#                   }
#syntaxe

    def no_bord_no_black(self):
        
        im = cv2.imread("couocu.png")
        y = 0
        for x in range(im.shape[0]):
            for y in range(im.shape[1]):
            
                if im[x,y][0] == 255 and im[x,y][1] == 255 and im[x,y][2] == 255:
                    y+=1
                    x = 0
                    break
                else:
                    im[x,y] = [0,0,0]

        cv2.imshow("couocu.png", im)
        cv2.imwrite("uu.png", im)

        
    def no_bord_no_black_gauche(self):
        im = cv2.imread("uu.png")

        y = 0
        for x in range(-im.shape[0],im.shape[0]):
            for y in range(0,im.shape[1]):
              
                if im[x,y][0] == 255 and im[x,y][1] == 255 and im[x,y][2] == 255:
                    x = -im.shape[0]
                    y+=1
                    
                else:
                    im[x,y] = [0,0,0]
                
        cv2.imshow("couocu.png", im)
        cv2.imwrite("uu.png", im)
        #marche pas ca sarrete en plein milieu fais chier
            
    def recup_lum(self):

        im = cv2.imread("yoyo.png")
        liste = []
        for x in range(im.shape[0]):
            for y in range(im.shape[1]):
                if im[x,y][0] < 200 and im[x,y][1] < 200 and im[x,y][2] < 200:
                    im[x,y] = [0,0,255]

        #cv2.imshow("couocu.png", im)



yo = irl_yeux()
#yo.position_yeux()
#yo.transforme_image()
#yo.yeux()
#yo.contour()
yo.no_bord_no_black()
yo.no_bord_no_black_gauche()
#yo.recup_lum()





























