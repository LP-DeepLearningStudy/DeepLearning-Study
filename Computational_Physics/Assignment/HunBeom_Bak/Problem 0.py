# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 15:00:03 2017

@author: Hunbeom Bak
"""
import matplotlib.pyplot as plt
import numpy as np


#Problems

#0 
x= np.linspace(0,10,100)
a=x**4*np.exp(-2*x)
b=(x**2*np.exp(-x)*np.sin(x**2))**2

plt.figure()
plt.plot(x,a,'b-',x,b,'r-')
plt.xlabel('x')
plt.legend(['(a)','(b)'],loc='upper right')
plt.title('Problem 0-0')
plt.show()

#1~3 은 파일이 없으므로 패스

#4 뭔말일까



#5 자유낙하
t=np.linspace(0,3,1000)
g=np.array([10])+0*t
v=15-g*t
x=15*t-1/2*g*t**2


a=plt.figure().add_subplot(3,1,1)
a.plot(t,g,'g')
plt.ylabel('Acceleration')
V=plt.figure().add_subplot(3,1,2)
V.plot(t,v,'b')
plt.ylabel('Velocity')
p=plt.figure().add_subplot(3,1,3)
p.plot(t,x,'r')
plt.ylabel('Positon')
plt.xlabel('Time')

plt.show()





