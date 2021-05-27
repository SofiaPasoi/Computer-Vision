#Pasoi Sofia, 2798, 6o etos
from matplotlib import pyplot as plt
from decimal import Decimal
from PIL import Image
import numpy as np
import sys
from matplotlib import rc
from matplotlib import image as mpimg
#elegxei an h eikona einai egxrwmi
def isColored(img,rows,columns):
    if(len(img.shape)==3):
        return True
    elif(len(img.shape)==2):
        return False

#an h eikona einai egxrwmi pairnei to meso oro twn rgb kai ton bazei stin timi tou pixel
#an den einai epistrefei tin idia tin eikona
def imageProccessing(img,rows,columns):
    colored=np.zeros([rows,columns])
    if(isColored(img,rows,columns)):  
        img=Decimal(img)
        for m in range (0,rows):
            for n in range (0,columns):
                colored[m][n]=(img[m][n][0]+img[m][n][1]+img[m][n][2])/3 
        return colored
    else: 
        return img


#katwfliwnei thn eikona symfwna me th synartisi katwfliwsis g(x) pou exoume apo ti thewria
def thresholding(new_image,rows,columns,threshold):
    timage= np.zeros([rows,columns])
    for m in range (0,rows):
        for n in range (0,columns):
            pixelValue=new_image[m,n]
            if(pixelValue<=threshold):
                timage[m,n]=0 #an i timi tou pixel einai<= apo to katwfli dinei sto pixel tin timi 0, diladi mauro
            else:
                timage[m,n]=255  #an i timi tou pixel einai >= apo to katwfli dinei sto pixel tin timi 255, diladi aspro
    return timage

#emafanizei kai apothikeuei tin eikona
def printImage(thr,filename,threshold):
    plt.ylim(thr.shape[0],0)
    plt.xlim(0,thr.shape[1])
    plt.subplots_adjust(left=0.1,bottom=0.19,right=0.9,top=0.96)#rythmizw poy ua emfanizetai h eikona
    s="threshold: " + str(threshold)
    plt.xlabel(s) #bazw lezanta tin timi tou katwfli
    plt.imshow(thr,cmap="gray")
    plt.show()
    Image.fromarray(thr.astype(np.uint8)).save(filename)#apothikeuei thn eikona 


def main():
    img=np.array(Image.open(sys.argv[1]))  
    rows=img.shape[0]
    columns=img.shape[1]
    str=sys.argv[2]
    threshold=int(sys.argv[3])#pairnw to prwto katwfli apo ta 5 poy thelw kai tha ypologisw ta ypoloipa
    #to katwfli prepei na einai anamesa sto 0 kai to 255
    #epeidi egw thelw 5 katwfli, diairw to 255/5=51
    #ara to prwto mou katwfli prepei na exei times apo 0 ews 51
    #to 2o katwfli tha exei timi isi me 2*(prwto katwfli)
    #antistoixa tha ypologistoun kai ta alla
    if(threshold>=0  and  threshold<=255): 
        new_image=imageProccessing(img, rows, columns)
        thr=thresholding(new_image, rows,columns, threshold)
        printImage(thr,str,threshold)#tha emfanisei kai tha apothikeusei 5 katwfliwmenes eikones
        #h kathe eikona tha exei onoma auto pou tha dinw ws eisodo mazi me enan apo tous arithous
        #0,1,2,3,4 wste na ksexwrizoun kai na apothikeuontai kai oi 5
        

main()