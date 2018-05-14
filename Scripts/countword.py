# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 21:38:05 2018

@author: hand
"""


def counter(str):
    abc = ['a', 'b', 'c', 'd', 'e',
           'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o',
           'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z']
    list = [0]*26
    str1 = str.lower()
    for i in str1:
        if i in abc:
            n=str1.count(i)
            list[abc.index(i)]=n
    return list


if __name__ ==  "__main__":
    str = input()
    print(counter(str))