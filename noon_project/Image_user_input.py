# importing the modles.

import imagehash
from PIL import ImageChops , Image , ImageStat
from fuzzywuzzy import fuzz   
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os 
import pandas as pd 
import urllib.request

# this is to store all the images into array_pics .  
directory = 'catus_pics'
array_pics = []
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        array_pics.append(f) 

# input the image you want to compare rest of the images with . 
main_str =  input("path of file in system.") 
main_img = Image.open(main_str) 




def Image_hash(main_img , array_pics) : 
   """
    qualities : 
         this will compare the structure of images , 
         it will not consider colors , brightness . nor the immer details inside the main boundry of 
         the obejct .  

         In this method always remove the background before working .  

    bacis working  : 
      This is a function that converts the image into a 8*8 grid , 
      then it makes the image into grey scale ,
      then the intergers are compared on the pixel values . 

    Return type : 
      It is a array of tuples , that has the image comapred , percentage similarity in the tuple respectively . 
   """
   img1_hash = imagehash.phash(main_img) 
   output = []
   for i in range(len(array_pics)) :   
       img2 = Image.open(array_pics[i])
       img2_hash = imagehash.phash(img2)  
       
       diff = (img1_hash - img2_hash )/len(img1_hash.hash)**2
       ans = (1-diff)*100
       tup = (img2,ans)  
       print("This is the pertentage similarity in the image hash ", ans) 
       output.append(tup)

   return output 

def image_pix_diff(main_img , array_pics ) :
    """
       Qualities :  
        Using this method we simply compare the diffrence in the pixels of the image , 
        this considers the colors , brightness , and the background .   
        It is best to isolate the main object from the image to make use of it . 

       Basic Working : 
          find the diffrence in the pixels , 
          then to  calculate the percentage diffrence , take the mean along all the three axis . then divide 
          by the number of axis , 
          then finally multiply of 255 

       Return type : 
       It is a array of tuples , that has the image comapred , percentage similarity in the tuple respectively .
    """ 
    output = []
    for i in range(len(array_pics)) :
        img2 = Image.open(array_pics[i])
        diff = ImageChops.difference(main_img, img2) 
        stat =  ImageStat.Stat(diff)
        print("this is the stat mean : ",stat.mean) 
        diff_ratio = sum(stat.mean) / (len(stat.mean) * 255)
        similar = 1-diff_ratio  
        print("This is the percentage similarity : " , similar*100,"%")  
        output.append((img2,similar*100))

    return output

function_type = str(input("if you want to comapre by shape type 'hash' , and if by all the featuers like colors,brightness then type 'diff' : "))

output = []
if function_type == "hash" : 
    output = Image_hash(main_img , array_pics) 
else :  
    output = image_pix_diff(main_img , array_pics) 

def plotting(main_img,output, function_type) :  
       for i in range(len(output)) : 
            img2 = output[i][0] 
            
            plt.subplot(1,3,1)
            plt.imshow(main_img) 
            plt.subplot(1,3,2)
            plt.title("the percentage similarity is : {}".format(output[i][1])) 
            plt.imshow(img2) 
            if(function_type == "diff") :  
                 plt.subplot(1,3,3) 
                 diff = ImageChops.difference(main_img , img2) 
                 plt.imshow(diff) 
            plt.show() 
plotting(main_img , output , function_type)
      
dict = {}
dict[main_str] = output 

"""
  A -> B,c,d
  dict[A_url] = {{b_url,per} , {c_url,per}}
"""