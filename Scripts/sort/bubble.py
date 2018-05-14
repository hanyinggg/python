# -*- coding: utf-8 -*-
"""
Created on Thu May 10 22:50:46 2018

@author: hand
"""
import random
L =[random.randint(1,1000000000) for i in range(500)]
for n in range(1, len(L)):
    for i in range(len(L)-n):
        if L[i] > L[i+1]:
            L[i], L[i+1] = L[i+1], L[i]
print(L)
        