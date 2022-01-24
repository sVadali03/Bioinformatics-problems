# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 14:34:06 2022

@author: Supri
"""

with open('dna strands.txt','r') as dna:
    dna_lst = [x for x in dna.readlines()]
    zipped_lst = list(zip(dna_lst[0],dna_lst[1]))
    ham_distance = 0
    for a,b in zipped_lst:
        if a!=b:
            ham_distance+=1
        else:
            continue
    print(ham_distance)