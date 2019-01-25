from PIL import ImageGrab
from PIL import *
from PIL import Image
import time
import shutil
import os
from numpy import *
from cv2 import *
import matplotlib.pyplot as plt
from outils_fichier import *
import os



class image:

        
    def capture_ecran(self, i):

        self.i = i
        liste = []
        self.name = str(self.i)+".png"
        self.name1 = str(self.i)+"_1.png"
        self.name2 = str(self.i)+"_2.png"
        self.name3 = str(self.i)+"_3.png"
        self.name4 = str(self.i)+"_4.png"
        self.name5 = str(self.i)+"_5.png"
        self.name6 = str(self.i)+"_6.png"
        
        img = ImageGrab.grab().convert("LA") 
        self.image = img.save(self.name)
        
        img1 = ImageGrab.grab()
        self.image1 = img1.save(self.name1)
        print(self.name1)

        
    def figure(self):
        
        
        self.name5 = str(self.i)+"_5.png"
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        img = cv2.imread(r"C:\Users\jeanbaptiste\video\{}".format(self.name1))
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]

            crop = img[y:h+y, x:w+x]
            
        cv2.imwrite(self.name5, img)
        


    def cadrage(self):
        
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
        print(self.name)
        img = cv2.imread(r"C:\Users\jeanbaptiste\video\{}".format(self.name))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            
            h1 = img.shape[1] - 1
            cv2.rectangle(img,(x-w,y+h),(x+w+w, y+h1), (0,0,255),2)#corps


            cv2.rectangle(img,(x-w,y+h),(x, y+h1),(0,0,255),2)#corps gauche
            
            cv2.rectangle(img,(x+w, y+h),(w+x+w, y+h1),(0,0,255),2)#corps droit
            
            cv2.rectangle(img,(x,y),(x+int(round(w/2)), y+h),(0,0,255),2)#gauche tete
            cv2.rectangle(img,(x+int(round(w/2)),y) ,(x+w, y+h),(0,0,2550),2)#droite tete



            cv2.rectangle(img,(x+x,y),(x+w, y+h),(0,0,255),2)#zone1 de tete
            cv2.rectangle(img,(w,y),(x, y+h),(0,0,255),2)#zone2 de tete
            
            self.crop = img[y:h1 ,x-w:x+w+w]

        cv2.imwrite(self.name2, img)


        
    def cadrage_coul(self):
        
        
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

        img = cv2.imread(r"C:\Users\jeanbaptiste\video\{}".format(self.name1))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            
            h1 = img.shape[1] - 1
            cv2.rectangle(img,(x-w,y+h),(x+w+w, y+h1), (0,0,255),2)#corps


            cv2.rectangle(img,(x-w,y+h),(x, y+h1),(0,0,255),2)#corps gauche
            
            cv2.rectangle(img,(x+w, y+h),(w+x+w, y+h1),(0,0,255),2)#corps droit

            cv2.rectangle(img,(x,y),(x+int(round(w/2)), y+h),(0,0,255),2)#gauche tete
            cv2.rectangle(img,(x+int(round(w/2)),y) ,(x+w, y+h),(0,0,255),2)#droite tete

            cv2.rectangle(img,(x+x,y),(x+w, y+h),(0,0,255),2)#zone1 de tete
            cv2.rectangle(img,(w,y),(x, y+h),(0,0,255),2)#zone2 de tete
            
            self.crop = img[y:h1 ,x-w:x+w+w]

        cv2.imwrite(self.name6, img)




        
    def transforme_image(self):
        
        
        image_pts = cv2.imread(self.name2, 0)
        edges = cv2.Canny(image_pts,100,200)
        plt.subplot(122),plt.imshow(edges,cmap = 'gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    
        cv2.imwrite(self.name3, edges)



        fichier.deplacer(self, r"C:\Users\jeanbaptiste\video",
                         self.name, r"C:\Users\jeanbaptiste\video\image")
        
        fichier.deplacer(self, r"C:\Users\jeanbaptiste\video",
                         self.name1,  r"C:\Users\jeanbaptiste\video\image_coul")
                        
        fichier.deplacer(self, r"C:\Users\jeanbaptiste\video",
                         self.name2,  r"C:\Users\jeanbaptiste\video\crop")
        
        fichier.deplacer(self, r"C:\Users\jeanbaptiste\video",
                         self.name5,  r"C:\Users\jeanbaptiste\video\tronche_coul")
                        
        fichier.deplacer(self, r"C:\Users\jeanbaptiste\video",
                         self.name6,  r"C:\Users\jeanbaptiste\video\crop_cool")
        
        fichier.deplacer(self, r"C:\Users\jeanbaptiste\video",
                        self.name3, r"C:\Users\jeanbaptiste\video\pts")





    def capture_temps_reel(self, i):

        
        self.i = i
        self.names = str(self.i)+".png"
        img = ImageGrab.grab()
        self.image = img.save(self.names)

        shutil.move(self.names, r"C:\Users\jeanbaptiste\video\irl")


    def capture_tete_reel(self):

        os.chdir(r"C:\Users\jeanbaptiste\video\irl")
        self.names2 = str(self.i)+"_2.png"
        
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        
        img = cv2.imread(r"C:\Users\jeanbaptiste\video\irl\{}".format(self.names))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]

        self.image = img.save(self.names2)
        shutil.move(self.names2, r"C:\Users\jeanbaptiste\video\tete_irl")











        
