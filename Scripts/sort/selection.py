# -*- coding: utf-8 -*-
"""
Created on Thu May 10 23:12:52 2018

@author: hand
"""

import random
L =[random.randint(1,10000) for i in range(1000)]

for i in range(0, len(L)):
    min = i
    for n in range(i+1, len(L)):
        if L[min] > L[n]:
            min = n
    L[i], L[min] = L[min], L[i]
print(L)
        
