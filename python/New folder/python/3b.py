# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 12:35:34 2023

@author: thota
"""

#program to find min, max, sum, cumulative sum of array####
import numpy as np

arr = np.array([12, 5, 23, 8, 15, 6, 9, 21])

#minimum and maximum
min_value = np.min(arr)
max_value = np.max(arr)
print("Array:", arr)
print("Minimum Value:", min_value)
print("Maximum Value:", max_value)

# sum 
sum_of_array = np.sum(arr)
print("Sum of the Array:", sum_of_array)

#cumulative sum
cumulative_sum = np.cumsum(arr)
print("Cumulative Sum of the Array:",cumulative_sum)

#slicing, integer and boolean array indexing
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Slicing
 
slice1 = arr[2:6]  
print("Sliced Array (arr[2:6]):", slice1)

#indexing
indices = np.array([1, 3, 8])
int_indexing = arr[indices]
print("Integer Array Indexing:", int_indexing)

# Boolean array indexing

mask = (arr % 2 == 0) 
bool_indexing = arr[mask]
print("Boolean Array Indexing (Even numbers):",bool_indexing)