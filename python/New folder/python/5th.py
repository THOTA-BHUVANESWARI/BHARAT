# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 07:45:37 2023

@author: thota
"""
# Create a white image using NumPy in Python 
import cv2
import numpy as np
array = np.zeros((400, 400, 3), dtype=np.uint8)
array[:,:] = [255, 255, 255]
cv2.imshow('white image',array)


















