# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 15:15:12 2017

@author: Hunbeom Bak
"""

from pylab import *
from scipy.optimize import brentq
from sympy import *

'''
#EX2.0.5

x=brentq(sin, 2,4)               #2와 4사이에 있는 x값중 sin을 0되게 하는값 출력

print(x, x-pi)


#부정적분
x=Symbol('x')
k=Symbol('k')
print (Integral(k*x,x))
y=Integral(k*x,x).doit()
print(y)

#적분
print(Integral(k*x,(x,0,2)).doit())         #x로 미분 범위는 0부터 2

#미분
t=Symbol('t')
z=5*t**2+2*t+8
print(z)

derit=Derivative(z, t)      #미분준비
print(derit)
zprime=derit.doit() #미분

print(zprime)               #미분한걸 그냥 출력

print(zprime.subs({t:1})) #미분한 것에 t=1 대입

'''
#Problem 2-2


x=Symbol('x')

print('(a)=',Integral(cos(x),(x,0,pi/2)).doit())

print('(b)=',Integral(1/x**2,(x,1,3)).doit())

print('(c)=',Integral(x**2+x+1,(x,2,4)).doit())

print('(d)=',Integral(cos(pi/2*x**2),(x,0,6.9)).doit())