# -*- coding: utf-8 -*-
"""
Created on Fri May 11 14:56:12 2018

@author: hand
"""
import random
def QuickSort(myList,left,right):
    if left >= right:
        return myList
    low = left
    high =right
    base = myList[left]
    while left < right:
        while (left < right) and (myList[right]>=base):
            right -=1
        myList[left] = myList[right]
        while (left < right) and (myList[left]<=base):
            left +=1
        myList[right] = myList[left]
    myList[right] = base
    QuickSort(myList, low, left-1)
    QuickSort(myList, left+1, high)
    return myList


myList =[random.randint(1,10000) for i in range(500)]
QuickSort(myList,0,len(myList)-1)
print(myList)
