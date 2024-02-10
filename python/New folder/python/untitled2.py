# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 13:49:09 2023

@author: thota
"""

"""
Created on Wed Aug 30 13:49:09 2023

@author: thota
"""
class parent:
    def __init__(self):
        self.x=int(input("enter x:"))
        self.y=int(input("enter y:"))
        def sub(self):
            sub=(self.x-self.y)
            print(sub)
class child(parent):
    def add(self):
        add=(self.x+self.y)
        print(add)
obj=child()
obj.add()
obj.sub()
        