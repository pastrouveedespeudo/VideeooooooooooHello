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

class irl_yeux:

    def position_yeux(self):
        eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        img = cv2.imread('homme.jpg')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)

            c = 0
            for (ex,ey,ew,eh) in eyes:

                cv2.rectangle(roi_color, (ex,ey),(ex+ew,ey+eh),(0,0,255),2)               
                c+=1

        cv2.imshow("yoyo.png", img)
yo = irl_yeux()
yo.position_yeux()
