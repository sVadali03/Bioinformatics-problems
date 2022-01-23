# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 13:24:31 2022

@author: Supri
"""

counter = 1
with open('sample.txt','r') as f:
    
    for line in f.readlines():
        if counter%2==0:
            print(line)
        counter +=1
        