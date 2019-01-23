class match:

    def match(self):
        
        img1 = cv2.imread ("bouboule1.png", 0)
        img2 = cv2.imread ("bouboule2.png", 0)

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
                print(c)
                img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:50],None, flags=2)
                plt.imshow(img3)
                plt.show()

        c = 0
