from lecture import *
from image import *
import threading 
import time
from traitement_image import *


class main:

    def lecture(self):
        lecture.play(self,"video4.mp4")


    def capture(self):
        a = True
        i = 1000
        while a:
            image.capture_ecran(self, i)
            image.figure(self)
            image.cadrage(self)
            image.cadrage_coul(self)
            image.transforme_image(self)
            time.sleep(5)
            i+=1
                        
    def matching(self):
        pass

    def tete(self):
        pass


                












if __name__ == "__main__":

    yo = main()

    

    t1 = threading.Thread(target = yo.lecture)
   
    t2 = threading.Thread(target = yo.capture)
 
    t3 = threading.Thread(target = yo.matching)


    t1.start()
    t2.start()
    t3.start()
 
  
  

  

    
    
    




  
