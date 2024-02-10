# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 12:39:08 2023

@author: thota
"""

#Write a python program to solve a linear matrix equation, or system of linear scalar equations.
import numpy as np
a=[[4,3],[-5,9]]
b=np.array(a)
c=np.linalg.inv(b)
print(c)
x=np.array([20,26])
y=np.linalg.inv(b).dot(x)
print(y)