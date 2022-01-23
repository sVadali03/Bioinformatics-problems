# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 13:16:30 2022

@author: Supri
"""

a = 4454 
b = 8637

total = 0
for num in range(a,b+1):
    if num%2==1:
        total = total+num
print(total)
        