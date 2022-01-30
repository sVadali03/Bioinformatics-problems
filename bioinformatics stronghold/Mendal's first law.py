# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 10:12:28 2022

@author: Supri
"""

# k  = number of homozygous dominant organisms
# n = number of heterozygous organisms
# m  = number of homozygous recessive organisms

def mendal_first_law(k,m,n):
    trait = k+m+n
    ress = n/trait * (n-1)/(trait-1)
    het_ress = m/trait * n/(trait-1) * .5
    ress_het = n/trait * m/(trait-1) * .5
    het_het = m/trait * (m-1)/(trait-1) * .25
    return 1 - (ress + het_ress + ress_het + het_het)

k = int(input())
m = int(input())
n = int(input())

print(round(mendal_first_law(k,m,n),5))
