# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 10:38:09 2017

@author: Hunbeom Bak
"""
'''
axis=[]
for i in range(100):
    axis.append(0.02*i) 
print(axis)
'''

#EX 1.7.1
def factorial(a):
    n=1
    c=1
    while n<=a:
       c=c*n
       n+=1
    return c

print('n!=',factorial(4))   

