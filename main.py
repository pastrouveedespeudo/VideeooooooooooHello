from lecture import *
from image import *
import threading 
import time

class main:

    def lecture(self):
        lecture.play(self,"video4.mp4")


    def capture(self):
        
        i = 10000
        a = True
        while a:
            
            image.capture_ecran(self, i)
            image.peau(self)
            image.cadrage(self,i)
            image.cadrage_coul(self,i)
            try:
                image.transforme_image(self)
            except:
                pass
            time.sleep(5)
            i+=1

    def traitement(self):
        
        traitement_image.recup_couleur(self)
        traitement_image.recupe_peau(self)
        traitement_image.contour1(self)
        traitement_image.nettoyage(self)
        traitement_image.contour2(self)
        #image.matches(self)

    












if __name__ == "__main__":

    yo = main()

    

    t1 = threading.Thread(target = yo.lecture)
    t2 = threading.Thread(target = yo.capture)
    t3 = threading.Thread(target = yo.traitement)

    
    t1.start()
    t2.start()
    t3.start()

  

    
    
    




  
