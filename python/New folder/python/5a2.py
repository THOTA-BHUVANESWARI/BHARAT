# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 12:43:27 2023

@author: thota
"""

import cv2
path = r"C:\Users\thota\OneDrive\Pictures\girl-g1513bbfb7_640.jpg"
image = cv2.imread(path)

cv2.imshow("girl-g1513bbfb7_640)", image)
cv2.waitKey(0)
cv2.destroyAllWindows()