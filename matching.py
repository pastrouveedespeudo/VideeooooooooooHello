import os

class match:

    def match_pouce(self, path1, path2):

        self.path1 = path1
        self.path2 = path2
        
        os.chdir(self.path1)
        
        liste1 = os.listdir()
        for i in liste1:
            shutil.move(i, self.path2)        

        os.chdir(self.path2)
        liste2 = os.listdir(self.path2)
        
        for i in liste1:

            cv2.imread(i)
            cv2.imread(liste2[-1])

            orb = cv2.ORB_create()

            kp1, des1 = orb.detectAndCompute(img1,None)
            kp2, des2 = orb.detectAndCompute(img2,None)

            bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
            matches = bf.match(des1,des2)

            matches = sorted(matches, key = lambda x:x.distance)

            c = 0
            for match in matches:
                c+=1
                
            if c > 100:
                print("y'a eu un pouce")
                #marquer sur la video

            c = 0

        for i in liste1:
            shutil.move(i, self.path1)     
