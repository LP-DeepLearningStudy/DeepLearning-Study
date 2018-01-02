# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 17:02:45 2017

@author: Hunbeom Bak
"""

import numpy as np
import matplotlib.pyplot as plt


#1-1  
#10부터 20까지 제곱 나열
def square():
    a=[]
    for i in range(10,21):
        a.append(i**2)   
    return a    
print('10부터 20까지의 제곱',square())

#1.1 
#피보나치 수열

def fibonachi(a):
        b=[]
        for i in range(a):
            if i<=1:
                b.append(1)
            else:
                b.append(b[i-1]+b[i-2])
        return b     

print('피보나치수열:',fibonachi(10))

#1.2 
#포탄받아라


def Y(a,b):
    #a:처음위치, b:처음속도
    t=[]
    y=[]
    g=9.8
    for i in range(51):
        t.append(0.1*i)
        y.append(a+b*t[i]-0.5*g*t[i]**2)    
    return y
        
plt.plot(Y(0,0))
plt.show()
'''
#1.3
def energy(L1):    
    pi=3.1415
    h=1.05457*10**(-34)
    m=9.109*10**(-31)
    L2=2*L1
    L3=4*L1
    for i in range(1,11):
        for j in range (1,11):
            for k in range (1,11):
                E=((h*pi)**2/(2*m))*((i/L1)**2+(j/L2)**2+(k/L3)**2)
                print(i,",",j,",",k,":",E)
                
energy(1)
'''

#1.4
x=np.linspace(-200,200)
plt.plot(np.sinc(x))
plt.show()

#1.5
def Sum(n):
    s=0
    i=0
    while i<=n : 
        s=s+i
        i+=1
    return s    

print(Sum(4))

print(Sum(5))