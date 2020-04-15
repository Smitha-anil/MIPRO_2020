# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 13:40:12 2020

@author: marti
"""

######
# converting colored masks to numbers
# background = 0
# PED (blue) = 1
# SRF (red) = 2
# IRF (yellow) 3


# Packages
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
import matplotlib.image as mpimg
from PIL import Image
import scipy
from scipy import ndimage
from pathlib import Path
import os, sys
import glob
import pycm
from pycm import *
import cv2


MASK_PATH = 'fluids_all/mask/'

# reading masks - list of mask (2D arrays)
mask = [plt.imread(file) for file in sorted(glob.glob(MASK_PATH+'*.png'))] 

#imshow(mask[3])
#plt.show()
#print (mask[3])

# dimenisons
width=512
height=1024 
mask_number=1241 # number of masks in dataset

# color definition
#1st channel red value, 2nd channel green value, 3rd blue, 4th channel alpha is allways equal 255
# images are normilesed to values [0, 1] (division by 255) so max values are 1 (not 255)
yellow=np.array([1,1, 0, 1])
red=np.array([1,0, 0, 1]) 
blue=np.array([0,0, 1, 1])
    

# 4 classes: background=0, PED=1, SRF=2, IRF=3
# joining class values to pixel values (grayscale image + color masks) 
def fluids (mask):
    fluid = np.zeros((width,height))
    for j in range (0,width):
        for i in range (0,heigth):
            if (mask[i,j]==blue).all():
                fluid[i,j]=1
            elif (mask[i,j]==red).all():
                fluid[i,j]=2 
            elif (mask[i,j]==yellow).all():
                fluid[i,j]=3 
           
    return fluid

# mask_new - list of new masks after performing conversion from pixel values to class numbers
mask_new = [fluids(mask[0])]
for k in range (1,1241):
   mask_new.append(fluids(mask[k]))
    
# creating new folder "new_mask" nested in fluids_all
os.chdir('fluids_all/')
os.makedirs('new_mask')

# reading list of file id (filename) for masks
# filename is necessary to save with previous name (identical to raw image filename)
all_masks = os.listdir(MASK_PATH)

# saving masks in folder new_mask
for k in range (0,1241):
    cv2.imwrite(all_masks[k], mask_new[k])



    
   

