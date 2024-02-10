# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 12:37:50 2023

@author: thota
"""

# program to demonstrate use of ndim, shape, size, dtype.
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
# Finding the number of dimensions (ndim) of the array
num_dimensions = arr.ndim

# shape (number of rows and columns)
shape = arr.shape

#total elements 
num_elements = arr.size

# data type 
data_type = arr.dtype
print("Array:")
print(arr)
print("Number of Dimensions (ndim):", num_dimensions)
print("Shape:", shape)
print("Size:", num_elements)
print("Data Type (dtype):",data_type)