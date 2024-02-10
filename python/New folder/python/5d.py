# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 12:42:43 2023

@author: thota
"""

#Write a program to demonstrate the use of the reshape() method
import numpy as np
arr=np.arange(10)
print(arr.reshape(2,5))
print(arr.reshape(5,2))