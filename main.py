from lecture import *
from image import *
import threading 
import time

class main:

    def lecture(self):
        lecture.play(self,"video6.mp4")


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
            #image.matches(self)
            #image.ensemble_match(self)
            time.sleep(5)
            i+=1

            
        















if __name__ == "__main__":

    yo = main()

    t2 = threading.Thread(target = yo.capture)

    t1 = threading.Thread(target = yo.lecture)


    
    t1.start()
    t2.start()

  

    
    
    




  
