# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 14:29:45 2023

@author: thota
"""
class A:
    def __init__(self):
        self.a=int(input("enter a:"))
        self.b=int(input("enter b:"))
    def mul(self):
        mul=self.a*self.b
        print(mul)
class B:
    def __init__(self):
        self.c=int(input("enter c:"))
        self.d=int(input("enter d:"))
    def sub(self):
        sub=self.c-self.d
        print(sub)
class C(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
    def add(self):
        add=self.a+self.d
        print(add)
obj=C()
obj.mul()
obj.sub()
obj.add()
            