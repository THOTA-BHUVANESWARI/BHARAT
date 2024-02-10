# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 12:38:21 2023

@author: thota
"""

#Write a python program to find eigenvalues of matrice
import numpy as np
a=([[1,2,3],[4,5,6],[7,8,9]])
b=np.array(a)
x,y=np.linalg.eig(b)
print("eigen values:")
print(x)
print("eigen vector:")
print(y)
