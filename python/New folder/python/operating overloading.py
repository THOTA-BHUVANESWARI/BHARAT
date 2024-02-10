# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 12:56:02 2023

@author: thota
"""
class A:
    def __init__(self,name):
        self.name=name
    def __add__(self,name1):
        print(self.name+name1.name)
obj1=A('john');
obj2=A('ravi');
s=obj1+obj2;
print(s)
