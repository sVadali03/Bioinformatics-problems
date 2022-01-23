# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 19:52:19 2022

@author: Supri
"""
with open('dna to rna.txt','r') as dna:
    rna = dna.read().replace('T','U')
    print(rna)
#dna = "GATGGAACTTGACTACGTAAATT"

