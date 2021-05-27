from matplotlib import pyplot as plt
from matplotlib import image as mpimg
from decimal import Decimal
from matplotlib import rc
from PIL import Image
import numpy as np
import array as arr
import sys

#vriskw an o ariumos twn grammwn kai twn stilwn einai perittos h artios
#gia na vrw to mesaio stoixeio
#epistrefei tis syntetagmenes tou mesaiou shmeiou se 1 pinaka
def dimension(rows,columns):
    halfx=0 
    halfy=0
    if(rows%2==0):
        halfx=int(rows/2)
        if(columns%2==0):
            halfy=int(columns/2)
        elif(columns%2==1):
            halfy=int((columns+1)/2)
    elif(rows%2==1):
        halfx=int((rows+1)/2)
        if(columns%2==0):
            halfy=int(columns/2)      
        elif(columns%2==1):
            halfy=int((columns+1)/2)
    return halfx,halfy

#ftiaxnw ton pinaka me tis syntetagmenes twn shmeiwn
#o pinakas tha exei diastaseis 3Xgrammes*stiles
#to mesaio stoixeio ths eikonas tha exei syntetagmenes (0.0),
#p.x. edw oi diastaseis einai 101x101, ara  ta stoixeia edw tha pairnoyn
#times apo -50 ws 50 sin to mesaio stoixeio
#h prwti grammi einai oi syntetagmeni m kai h deuteri h n
#epistrefei twn pinaka auto
def coordinatesArray(tmp,rows,columns):
    rows1=tmp[0]
    columns1=tmp[1]
    mu=rows*columns 
    A=np.zeros([3, mu])
    tmp1=1-columns1
    a=1-rows1  
    b=1-columns1
    for m in range(0,3):
        for n in range(0,mu):
            if(m==0):
                if(n%101!=0):
                    A[m][n]=a
                    a=a+1
                else:
                    a=1-rows1
                    A[m][n]=a
                    a=a+1
            elif(m==1):      
                b=tmp1
                if(n==0):
                    A[m][n]=b
                elif(n%101!=0):               
                    A[m][n]=b
                elif(n%101==0):
                    tmp1=0
                    tmp1=b+1
                    A[m][n]=tmp1
            else:
                A[m][n]=1
    return A

#pairnei ton pinaka syntetagmenwn kai ton pollaplasiazei me tis parametrous tou metasximatismou
#briskei thn paremboli me tin synartisi round pou mas paei ston kontinotero akeraio
#prosthetei ayto pou eixe afairesei prin gia na kanei (0.0) to mesaio stoixeio
#ginetai o metasximatismos, h paremvoli kaisto telos oi syntetagmes exoyn tis idies times pou exoun kai 
#oi syntetagmenes tis arxikis eikonas
def newCoordinatesArray(A,rows,columns,a1,a2,a3,a4,a5,a6):
    mu=rows*columns 
    A1=np.zeros([3,mu])
    m1=int((rows-1)/2)
    n1=int((columns-1)/2)
    for m in range(0,3):
        for n in range(0,mu):
            if(m==0):
                x=A[0][n]*a1+A[1][n]*a2+A[2][n]*a3#metasximatismos
                A1[m][n]=round(x)#paremvoli
                
                if(A1[m][n]>=m1): # an i timi einai megaliteri apo ti megisti syntetagmeni m tin kanei isi me thn m
                    A1[m][n]=rows-1
                elif(A1[m][n]<=-m1):# an i timi einai mikroteri apo tin elaxisti syntetagmeni m tin kanei isi me 0
                    A1[m][n]=0
                else: 
                    A1[m][n]=A1[m][n]+m1# alliws prosthetei tin timi poy eixe afairesi prin
            elif(m==1):      
                y=A[0][n]*a4+A[1][n]*a5+A[2][n]*a6#metasximatismos
                A1[m][n]=round(y)#paremvoli
                
                if(A1[m][n]>=n1):# an i timi einai megaliteri apo ti megisti syntetagmeni n tin kanei isi me thn n
                    A1[m][n]=columns-1
                elif(A1[m][n]<=-n1):# an i timi einai mikroteri apo tin elaxisti syntetagmeni n tin kanei isi me 0
                    A1[m][n]=0
                else: 
                    A1[m][n]=A1[m][n]+n1# alliws prosthetei tin timi poy eixe afairesi prin
                
            else:
                A1[m][n]=1
    return A1

#kanei tin antistoixish twn timwn twn fwtoinothtwn tis arxikis eikonas stin kainouria
def newImg(A1,img,rows,columns):
    new=np.zeros([rows,columns])
    i=0
    j=0
    c=0
    for m in range(0,rows):
        for n in range(0,columns):
            i=int(A1[0][c])
            j=int(A1[1][c])
            new[m][n]=img[j][i]#ta sxolia gia auti ti grammi vriskontai sto telos tou kwdika
            c=c+1      
    return(new)

def printImage(thr, filename):
    plt.subplots_adjust(left=0.1, bottom=0.19, right=0.9, top=0.96)
    plt.imshow(thr,cmap="gray")
    plt.show()
    Image.fromarray(thr.astype(np.uint8)).save(filename)

def main():
    img=np.array(Image.open(sys.argv[1]))
    rows=img.shape[0]
    columns=img.shape[1] 
   
    str=sys.argv[2]
    a1=float(sys.argv[3]) 
    a2=float(sys.argv[4])
    a3=float(sys.argv[5])
    a4=float(sys.argv[6])
    a5=float(sys.argv[7])
    a6=float(sys.argv[8])

    tmp=dimension(rows, columns)
    print(tmp)
    A=coordinatesArray(tmp,rows,columns)
    A1=newCoordinatesArray(A,rows,columns,a1,a2,a3,a4,a5,a6)
    new=newImg(A1,img,rows,columns)
    
    printImage(new, str)

main()     

#sxolia gia tin grammi 116:
# epeidi otan ftiaxnw ton pinaka me tis syntetagmenes ton digemizw me ta stoixeia 
# kata stili kai oxi kata grammi(diladi diatrexw tin eikona katakorifa kai oxi orizontia)
# gia na parw ti swsti timi tou pixel apo tin arxiki eikona vazw antestramenes tis 
# syntetagmenes   


    
