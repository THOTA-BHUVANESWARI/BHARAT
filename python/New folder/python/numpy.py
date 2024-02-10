# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 14:26:19 2023

@author: thota
"""
import numpy as np
a=np.array([[1,3,2],[4,2,3],[4,7,5]])
print(a.trace())
print(np.linalg.matrix_rank(a))
print(np.linalg.det(a))
x,y=np.linalg.eig(a)
print("eigen values/n",x)
print("eigen values/n",y)
a=np.array([3,5])
b=np.array([6,7])
x=np.array([[3,5],[6,7]])
y=np.array([[4,6],[1,2]])
print("dot product of vectors/n",np.dot(x,y))
print("inner product of vectors/n",np.inner(x,y))
print("outer product of vectors/n",np.outer(x,y))