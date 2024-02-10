# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 13:49:12 2023

@author: thota
"""

class person:

     def __init__(self,name,height,weight,age):
         self.name=name;
         self.height=height;
         self.weight=weight;
         self.age=age;
     def get_bmi_weight(self):
         bmi=(self.weight) / (self.height**2)
         if (bmi<18.5):
             print("unhealthy")
         elif(bmi<24.9):
             print("health")
         else:
            print("obese")
obj=person(name=input(),age = int(input()),height = int(input()),weight = int(input()))
obj.get_bmi_weight()



             