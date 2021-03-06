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


    def recup_for_match(self):
        i = 9000
        while True:
            traitement_image.recup_couleur(self)
            traitement.recupe_peau(self)
            traitement.contour1(self)
            traitement.nettoyage(self)
            traitement.contour2(self, i)
            match.match_pouce(self, r"C:\Users\jeanbaptiste\video\pousse_pas_mélange2",
                r"C:\Users\jeanbaptiste\video\match")
            i+=1



    def capture_mouvement(self):
        a = True
        i = 6000
        while a:
            image.capture_temps_reel(self, i)
            image.capture_tete_reel(self)
            i+=1
    



    def tete(self):
        i = 150000
        
        while True:
            irl_tete.capture_ecran(self, i)
            irl_tete.crop_tete_irl(self)
            irl_tete.recup_couleur(self)
            irl_tete.recupe_peau(self)
            irl_tete.contour1(self)
            irl_tete.nettoyage(self)
            irl_tete.countour2(self)
            irl_tete.pts(self)
            irl_tete.gauche_ou_droite(self)
            


                












if __name__ == "__main__":

    yo = main()

    

    t1 = threading.Thread(target = yo.lecture)
   
    t2 = threading.Thread(target = yo.capture)

    t3 = threading.Thread(target = yo.recup_for_match)



    t5 = threading.Thread(target = yo.capture_mouvement)

    t1.start()
    t2.start()
    t3.start()

    t5.start()
 
  
  

  

    
    
    




  
