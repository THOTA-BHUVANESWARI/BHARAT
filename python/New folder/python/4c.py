# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 12:38:45 2023

@author: thota
"""

#Write a python program to find matrix and vector products (dot, inner, outer, product), matrix exponentiation
import numpy as np
a=np.array([7,8])
b=np.array([6,7])
x=np.array([[7,8],[6,7]])
y=np.array([[1,2],[4,5]])
print("dot product:",np.dot(x,y))
print("inner product",np.inner(x,y))
print("outer product:",np.outer(x,y))