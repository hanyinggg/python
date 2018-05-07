# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 14:55:46 2018

@author: hand
"""

from array import array
from random import random
floats2 = array('d')
fp = open('floats.bin','rb')
floats2.fromfile(fp,1000)
fp.close()    
print(floats2)
