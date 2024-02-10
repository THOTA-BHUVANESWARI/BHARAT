# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 12:41:17 2023

@author: thota
"""

#Convert a NumPy array to an image and Convert images to NumPy array
import matplotlib.pyplot as plot
from PIL import Image
import numpy as np
data=np.zeros((10,10,3),dtype=np.uint8)
data[:,:]=[0,0,50]
img=Image.fromarray(data,'RGB')
print(img)
plot.imshow(img)
img.save("python.png")
img.show()
img.data=Image.open("python.png")
img.arr=np.array(img.data)
print(img.arr)