# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 12:42:04 2023

@author: thota
"""

#Perform Sorting, Searching and Counting using Numpy methods
import numpy as np
a=np.array([[12,15],[10,1]])
arr=np.sort(a,axis=0)
print("along first axis:\n",a)
b=np.count_nonzero(a)
print("the number of elements in the matrix a is :\n",b)
c=np.where(a)