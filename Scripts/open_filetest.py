# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 15:29:46 2018

@author: hand
"""

file = open('gulong.txt','w')
file.write('古龙是我非常喜欢的一位武侠作者')
file.close()
f = open('gulong.txt','r')
p1 = f.read(5)
print(p1)




