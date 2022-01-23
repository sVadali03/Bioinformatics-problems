# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 19:09:46 2022

@author: Supri
"""

with open('Counting DNA Nucleotides.txt','r') as dna:
    dna_list = [x for x in dna.read()]
    adenine_count = dna_list.count('A')
    cytosine_count = dna_list.count('C')
    guanine_count = dna_list.count('G')
    thymine_count = dna_list.count('T')
    
    print(adenine_count,cytosine_count,guanine_count,thymine_count)

    
   