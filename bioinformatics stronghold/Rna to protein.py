# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 11:30:53 2022

@author: Supri
"""

rna_codon = {"UUU":"F","UUC":"F","UUA":"L","UUG":"L","UCU":"S",\
            "UCC":"S","UCA":"S","UCG":"S","UAC":"Y","UAU":"Y","UAA":"Stop",\
            "UAG":"Stop","UGU":"C","UGC":"C","UGA":"Stop","UGG":"W",\
            "CUU":"L","CUC":"L","CUA":"L","CUG":"L","CCU":"P","CCC":"P",\
            "CCA":"P","CCG":"P","CAU":"H","CAC":"H","CAA":"Q","CAG":"Q",\
            "CGU":"R","CGC":"R","CGA":"R","CGG":"R","AUU":"I","AUC":"I",\
            "AUA":"I","AUG":"M","ACU":"T","ACC":"T","ACA":"T","ACG":"T",\
            "AAU":"N","AAC":"N","AAA":"K","AAG":"K","AGU":"S","AGC":"S",\
            "AGA":"R","AGG":"R","GUU":"V","GUC":"V","GUA":"V","GUG":"V",\
            "GCU":"A","GCA":"A","GCC":"A","GCG":"A","GAC":"D","GAU":"D","GAA":"E","GAG":"E",\
            "GGU":"G","GGC":"G","GGA":"G","GGG":"G"}
    
def translation(string):
    protein = ''
    for x in range(0,len(string),3):
        l = rna_codon[string[x:x+3]]
        if l=='Stop':
            break
        else:
            protein+=l
    return protein

with open('Rna to protein.txt') as rna:
    string = rna.readline().strip()
print(translation(string))
        