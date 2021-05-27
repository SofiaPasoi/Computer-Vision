#Pasoi Sofia, 2798, 6o etos
from matplotlib import pyplot as plt
from decimal import Decimal
from PIL import Image
import numpy as np
import sys
from matplotlib import rc
from matplotlib import image as mpimg

#apofasizei tin nea timi tou pixel
def thresholding(pixelValue,threshold):
    if(pixelValue<=threshold):
        timage=0 #an i timi tou pixel einai<= apo to katwfli dinei sto pixel tin timi 0, diladi mauro
    else:
        timage=255  #an i timi tou pixel einai >= apo to katwfli dinei sto pixel tin timi 255, diladi aspro
    return timage

#elegxei an h eikona einai egxrwmi
def isColored(img):
    if(len(img.shape)==3):
        return True
    elif(len(img.shape)==2):
        return False

#an h eikona einai egxrwmi pairnei to meso oro twn rgb kai ton bazei stin timi tou pixel
#an den einai epistrefei tin idia tin eikona
def imageProccessing(img):
    rows=img.shape[0]
    columns=img.shape[1]
    colored=np.zeros([rows,columns])
    if(isColored(img)):  
        #img=Decimal(img)
        for m in range (0,rows):
            for n in range (0,columns):
                colored[m][n]=(img[m][n][0]+img[m][n][1]+img[m][n][2])/3#pairnei to meso oro twn r g b
        return colored
    else: 
        return img


def ypologise_antikeimeniki_otsu(neighborhood, k):
    pixels_tmima1 = neighborhood[neighborhood < k]#ftiaxnw ta 2 tmimata
    pixels_tmima2 = neighborhood[neighborhood >=k]
    mu1 = np.mean(pixels_tmima1) #pairnw to meso twn tmimatwn
    mu2 = np.mean(pixels_tmima2)
    mu_synoliko = np.mean(neighborhood.flatten()) #pairnw to meso olis tis geitonias
    pi1 = len(pixels_tmima1) / (len(pixels_tmima1) + len(pixels_tmima2))
    pi2 = len(pixels_tmima2) / (len(pixels_tmima1) + len(pixels_tmima2))
    antikeimeniki_synartisi = pi1 * (mu1 - mu_synoliko)**2 + pi2 * (mu2 - mu_synoliko)**2
    return(antikeimeniki_synartisi)


def otsu_thresholder(neighborhood, pixelValue):
    kalytero_katwfli = 0
    kalyterh_timi = 0
    for i in range(0,neighborhood.shape[0]): #diatrexw ton pinaka me tis fwtinotites
        obj_otsu = ypologise_antikeimeniki_otsu(neighborhood, neighborhood[i]) #kalw tin otsu me ti geitonia gia kathe timi fwtinotitas twn pixels tis 
        if(obj_otsu > kalyterh_timi): #kanei ti megistopoihsh
            kalytero_katwfli = neighborhood[i]
            kalyterh_timi = obj_otsu
    res = thresholding(pixelValue,kalytero_katwfli)#kalw tin thresholding me tin timi tou pixel kai to katwfli gia na vrw tin timi tou neou pixel
    return(res) #epistrefw tin timi tou pixel

def imageThr(image,winrows,wincols,rows,columns): #analitika sxolia gia tin geitonia sto telos tou kwdika
    timage= np.zeros([rows,columns])
    m =winrows
    n=wincols
    if(m%2==0): 
        m=int(m/2 + 1)
        if(n%2==0):
            n=int(n/2 + 1)    
        else: 
            n=int(n/2 - 1/2)        
    else: 
        m=int(m/2- 1/2)
    
        if(n%2==0):
            n=int(n/2 + 1)    
        else:     
            n=int(n/2 - 1/2)
      
    for i in range(0, rows):
        for j in range(0,columns): #diatrexw tin eikona
            neighborhood=np.array([])
            for k in range(-n,n+1): #diatrexw ti geitonia
                a=np.array([])
                for z in range(-m,m+1):
                    if(i+k>=0): #ta ifs pragmatopoioun elegxous gia na min ksefugei h geitonia apo ta oria tis eikonas
                        if(i+k<rows):
                            if(j+z>=0):
                                if(j+z<columns):
                                    a=np.append(a, image[i+k][j+z], axis=None)
                if(len(a)!=0):   
                    neighborhood=np.append(neighborhood, a)
           
            thr_pixel=otsu_thresholder(neighborhood,image[i][j])#kalw tin otsu me ti geitonia kai me tin timi tou pixel kai mou epistrefei tin nea timi tou pixel
            
            timage[i][j]=thr_pixel #ftiaxnw tin katwfliwmeni eikona me tis nees times twn pixels
            
    return timage #epistrefw tin katw eikona

def printImage(thr,filename,window_size,img):
    plt.ylim(thr.shape[0],0)
    plt.xlim(0,thr.shape[1])
    plt.subplots_adjust(left=0.1,bottom=0.19,right=0.9,top=0.96)#rythmizw poy ua emfanizetai h eikona
    s="window_size of neighborhood: " + str(window_size)
    plt.xlabel(s) #bazw lezanta tin timi tou window_size
    #plt.imshow(img,cmap="gray")
    plt.imshow(thr,cmap="gray")
    plt.show()
    Image.fromarray(thr.astype(np.uint8)).save(filename)#apothikeuei thn eikona 


def main():
    img=np.array(Image.open(sys.argv[1])) 
    rows=img.shape[0]
    columns=img.shape[1]
    str=sys.argv[2]
    window_size=sys.argv[3]
    window_size=window_size.split("x")
    winrows=int(window_size[0])
    wincols=int(window_size[1])
    image=imageProccessing(img)
    thr=imageThr(image,winrows,wincols,rows,columns)
    printImage(thr,str,window_size,img)
  
main()
#########################
#sxolia gia tin geitonia
#1.thelw to pixel poy epeksergazomai na einai to mesaio ston pinaka tis geitonias
#2.ara tha parw apo to window_size pou edwse o xristis kai tha vrw posa stoixeia prepei na exei deksia aristera panw kai katw to pixel
#pairnw to window size kai vriskw ta misa twn grammvn kai twn sthlwn tou.
#p.x. : an dwsw window size 3x5 tha vrw oti tha exw 1 grammi panw kai katw apo to pixel kathws kai 2 sthles 
#apo deksia kai apo aristera tou.
#3.epeita elegxw an h geitonia mou vrisketai mesa sta oria tiw eikonas
#to pixel tha exei ti thesi i,j kai exw win size 3x5, elegxw gia paradeigma to pixel sta aristera tou i,j
#dhladh to i,j-1. Thelw loipon to j-1 na einai megalutero apo to 0, dhladh sti xeiroterh na vrisketai stin
#prwth sthlh. Antistoixa gia to deksia i,j+1 prepei to j+1 na einai mikrotero tou arithmou twn sthlwn.
#M ton idio tropo elegxw oli ti geitonia kai krataw mono ta pixels poy vriskontai mesa sta oria
#tis eikonas
