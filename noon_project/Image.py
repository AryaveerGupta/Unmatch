# importing the modles.
# math of imagehash , 

import imagehash
from PIL import ImageChops , Image , ImageStat
from fuzzywuzzy import fuzz   
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os 
directory = 'catus_pics'
array_pics = []
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        array_pics.append(f) 
    
for i in range(len(array_pics)-1) :  
   img1 = Image.open(array_pics[i])
   img2 = Image.open(array_pics[i+1]) 

   img1_hash = imagehash.phash(img1) 
   img2_hash = imagehash.phash(img2)
   diff = (img1_hash - img2_hash )
#    diff = (img1_hash - img2_hash )/len(img1_hash.hash)**2
#    print("This is the pertentage similarity in the image hash ", (1-diff)*100) 
   # diff = ImageChops.difference(img1, img2)
   # plt.subplot(1,3,3)
   # plt.imshow(diff) 
   # stat =  ImageStat.Stat(diff)
   # diff_ratio = sum(stat.mean) / (len(stat.mean) * 255)
   # similar = 1-diff_ratio
   # print(similar*100,"%")
   plt.subplot(1,3,1)
   plt.imshow(img1) 
   plt.subplot(1,3,2)
   plt.imshow(img2) 
   plt.show() 
   
    
# So  thinking to  
