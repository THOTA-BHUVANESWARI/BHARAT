# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 12:40:39 2023

@author: thota
"""


import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Create a NumPy array
arr = np.arange(0, 8, 1, dtype=np.uint8)  # Use uint8 to represent RGB values

# Reshape the array to 2x4x3, repeating the values to fill R, G, B channels
arr_reshaped = np.repeat(arr.reshape(2, 4, 1), 3, axis=2)
print("Array is:\n", arr_reshaped)

# Convert the NumPy array to an image
image = Image.fromarray(arr_reshaped, 'RGB')

print("Image is:\n", image)

# Display the image using matplotlib
plt.imshow(image)
plt.show()