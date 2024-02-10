# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 22:16:21 2023

@author: thota
"""

#Write a python program to find rank, determinant, and trace of an array.
import numpy as np
a=([1,2,3],[4,5,6],[7,8,9])
b=np.array(a)
print(b.trace())
print(np.linalg.matrix_rank(b))
print(np.linalg.det(b))






