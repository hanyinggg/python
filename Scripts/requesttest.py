# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 16:41:07 2018

@author: hand
"""

import requests
from bs4 import BeautifulSoup
import re
r = requests.get('https://book.douban.com/subject/1865089/comments/')
soup = BeautifulSoup(r.text,'lxml')
pattern = soup.find_all('p','comment-content')
for item in pattern:
    print(item.string)
    
    
    

