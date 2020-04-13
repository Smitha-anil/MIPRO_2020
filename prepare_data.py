# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 09:49:46 2020

@author: marti
"""

#######
#preparing data - split images and masks in train, dev and test folder randomly

import os
import random
import re
from PIL import Image

DATA_PATH = 'fluids_all'
IMAGE_PATH = 'fluids_all/images/'
MASK_PATH = 'fluids_all/masks/'

# Create folders to hold images and masks

folders = ['train_images', 'train_masks', 'val_images', 'val_masks', 'test_images', 'test_masks']


for folder in folders:
  os.makedirs(folder)
  
  
# Get all images and masks, sort them, shuffle them to generate data sets.

all_images = os.listdir(IMAGE_PATH)
all_masks = os.listdir(MASK_PATH)


all_images.sort(key=lambda var:[int(x) if x.isdigit() else x 
                                for x in re.findall(r'[^0-9]|[0-9]+', var)])
all_masks.sort(key=lambda var:[int(x) if x.isdigit() else x 
                               for x in re.findall(r'[^0-9]|[0-9]+', var)])


random.seed(240)
random.shuffle(all_images)


# Generate train, val, and test sets for images

# split: 80% train, 10%vval, 10% test
# all: 1241 images -> 993 train, 124 val, 124 test
train_images = all_images[:993]
val_images = all_images[993:1117]
test_images = all_images[1117:]


# Generate corresponding mask lists for masks

train_masks = [f for f in all_masks if f in train_images]
val_masks = [f for f in all_masks if f in val_images]
test_masks = [f for f in all_masks if f in test_images]


#Add train, val, test images and masks to relevant folders


def add_images(dir_name, image):
  
  img = Image.open(IMAGE_PATH+image)
  img.save('{}'.format(dir_name)+'/'+image)
  
  
  
def add_masks(dir_name, image):
  
  img = Image.open(MASK_PATH+image)
  img.save('{}'.format(dir_name)+'/'+image)


  
  
image_folders = [(train_images, 'train_images'), (val_images, 'val_images'), 
                 (test_images, 'test_images')]

mask_folders = [(train_masks, 'train_masks'), (val_masks, 'val_masks'), 
                (test_masks, 'test_masks')]

# Add images

for folder in image_folders:
  
  array = folder[0]
  name = [folder[1]] * len(array)

  list(map(add_images, name, array))
         
    
# Add masks

for folder in mask_folders:
  
  array = folder[0]
  name = [folder[1]] * len(array)
  
  list(map(add_masks, name, array))
