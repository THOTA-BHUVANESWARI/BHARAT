# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 13:49:09 2023

@author: thota
"""
class A:
    def __init__(self):
        self.a=int(input("enter a:"))
        self.b=int(input("enter b:"))
class B(A):
    def add(self):
        add=self.a+self.b
        print(add)
    def sub(self):
        sub=self.a-self.b   
        print(sub)
class C(B):
    def mul(self):
        mul=self.a*self.b
        print(mul)
obj=C()
obj.add()
obj.sub()
obj.mul()

        