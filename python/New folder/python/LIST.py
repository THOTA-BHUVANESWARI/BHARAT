# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 13:35:23 2023

@author: thota
"""

L1=['DBMS','DSA','DMS']
L2=['JAVA','PYTHON','CO','PYTHON']
L1.append('beee')
print(L1)
L1.clear()
print(L1)
X=L2.copy()
print(X)
X=L2.count('PYTHON')
print(X)
L3=['labs','theory','exams']
L3.extend(L2)
print(L3)
X=L2.index('PYTHON')
print(X)
L2.insert(3,'physics')
print(L2)
L2.pop(4)
print(L2)
L2.remove('JAVA')
print(L2)
L2.reverse()
print(L2)
L2.sort()
print(L2)