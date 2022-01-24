# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 14:08:15 2022

@author: Supri
"""

with open("dna compliment.txt",'r') as dna:
    #dna_comp = { 'A':'T', 'T':'A', 'G':'C','C':'G' }
    new_strand = ''
    dna_string = dna.read()
    for x in dna_string:
        if x=='A':
            new_strand+='T'
        elif x=='T':
            new_strand+='A'
        elif x=='G':
            new_strand+='C'
        elif x=='C':
            new_strand+='G'
        
    
    print(new_strand[::-1])