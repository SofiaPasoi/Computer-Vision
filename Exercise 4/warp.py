#Pasoi Sofia, 2798, 6o etos
import numpy as np
from cv2 import cv2
import sys
from matplotlib import pyplot as plt


M=[]
def mousePosition(event,x,y,flags,params):
    global M
    N=[]
    if event == cv2.EVENT_FLAG_LBUTTON: # epilegw ta 4 shmeia patwntas aristεro click
    #kai ta vazw se ena pinaka
        N.append(x)
        N.append(y)
        #vazw ton katnena pinaka se enan allo,wste na ftiaksw ena pinaka apo pinakes me tis 
        #syntetagmenes
        M.append(N)    
    elif event==cv2.EVENT_FLAG_RBUTTON:# gia na emfanistei h nea eikona pataw deksi click
        # ftiaxnw ton pinaka me tous syntelestes twn a1-a8
        #kathe grammi toy pinaka einai kai 1 eksiswsi
        #o a einai pinakas 8x8 giati to a9 kseroume oti einai iso me 1
	#o pinakas kataskeyastike vasi oswn sxoliastikan sto mathima kai twn shmeiwsewn
        a=np.array([[M[0][0],M[0][1],1,0,0,0,0,0,],
            [0,0,0,M[0][0],M[0][1],1,0,0,],
            [M[1][0],M[1][1],1,0,0,0,-M[1][0]*1000,-M[1][1]*1000],
            [0,0,0,M[1][0],M[1][1],1,0,0],
            [M[2][0],M[2][1],1,0,0,0,0,0],
            [0,0,0,M[2][0],M[2][1],1,-M[2][0]*1000,-M[2][1]*1000],
            [M[3][0],M[3][1],1,0,0,0,-M[3][0]*1000,-M[3][1]*1000],
            [0,0,0,M[3][0],M[3][1],1,-M[3][0]*1000,-M[3][1]*1000]])
        #o pinakas b periexei tis nees syntetagmenes twn 4 shmeiwn
        b=np.array([0,0,1000,0,0,1000,1000,1000])
        N=np.linalg.solve(a,b) #h solve antistrefei ton a, epeita ton pol/zei me ton b
        #kai vriskei ton pinaka metasxhmatismoy
        F = np.empty([3,3])
        #vazw tis times pou vrika se ena pinaka 3x3 pou einai o pinakas metasximatismou
        F[0][0]=N[0]
        F[0][1]=N[1]
        F[0][2]=N[2]
        F[1][0]=N[3]
        F[1][1]=N[4]
        F[1][2]=N[5]
        F[2][0]=N[6]
        F[2][1]=N[7]
        F[2][2]=1
        out=str(sys.argv[2])
        str1="/home/adminn/Desktop/Warp(Askisi3)/"+ out #dialegw pou tha apothikausw ti nea eikona
        dst = cv2.warpPerspective(img,F,(1000,1000)) # pairnei tin eikona, ton pinaka metasximatismou
        #to megethos tis neas eikonas kai kanei tin antistoixisi twn syntetagmenwn twn pixels, kai
        #epistrefei ti nea eikona
        cv2.imshow("image", dst)# emfanizw ti nea eikona
        #plt.imshow(dst)
        #plt.show()
        cv2.imwrite(str1,dst)#apothikeyw ti nea eikona


image=sys.argv[1]
out=sys.argv[1]
img = cv2.imread(image)
cv2.startWindowThread()
cv2.namedWindow("image",cv2.WINDOW_NORMAL)#ftiaxnw to parathyro wste na emfanizetai se kanoniko megethos
cv2.imshow("image", img) #emfanizw tin eikona wste na epileksei o xristis ta shmeia
print("aristero click stis 4 gwnies tis eikonas")
print("deksi click gia na emfanistei h nea eikona")
print("pata to esc gia na termatisei")
cv2.setMouseCallback("image", mousePosition)
k=cv2.waitKey(0)
if(k==27): #to 27 einai to id tou esc prepei na to patisw meta tin emfanisi tis eikonas gia na stamatisw to terminal
    cv2.destroyAllWindows()



