# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 14:41:51 2017

@author: Hunbeom Bak
"""

from numpy import *
from numpy.linalg import*
import matplotlib.pyplot as plt
from scipy.optimize import brentq
from random import *

#3-0
#ax=b
a= array([[1/5,1,1,1,-1,-1],[1,0,1,-1,5,1],[-1,-3,2,-1,-1,-1],[0,5,0,1,1,2],[1,-2,3,1/2,0,0],[1/2,-2,-2,-1,1,-6]])
b=array([24.1312,46.2798,-61.8372,31.1466,51.2106,-5.7008])
x = linalg.solve(a, b)
print(x)

#3-1
#공던지기
g=9.8
v0=5
y0=3
t=linspace(0,1.5, 100)

y=y0+v0*t-0.5*g*t**2

plt.plot(t,y,'b-')
plt.title('problem 3-1')
plt.xlabel('Time')
plt.ylabel('y(t)')
plt.show()

#3-2
def spring(yo,k,m):
    t=linspace(0,10, 333)
    w0=(k/m)**(1/2)
    y=yo*cos(w0*t)
    
    plt.plot(t,y)
    plt.title('Problem 3-2')
    plt.xlabel('time')
    plt.ylabel('position')
    plt.show()
    
spring(6,3.5,1)

#3-3 
def spring_phasespace(yo,k,m):
    t=linspace(0,10, 1000)
    w0=(k/m)**(1/2)
    y=yo*cos(w0*t)
    yprime=-yo*w0*sin(w0*t)
    
    plt.plot(y,yprime)
    plt.title('phasespace')
    plt.xlabel('positon')
    plt.ylabel('velocity')
    plt.show()

spring_phasespace(6,3.5,1)

#3-4
def damping(yo,k,m):
    t=linspace(0,50, 1000)
    w0=(k/m)**(1/2)
    r=0.05 #미급감쇠
    q=(r**2-w0**2)**(1/2)
    wd=(w0**2)**(1/2)
    y=exp(-r*t)*(y0*sin(wd*t))
    
    plt.plot(t,y,'g-')
    plt.title('Problem 3-4 Position')
    plt.xlabel('time')
    plt.ylabel('position')
    plt.show()
    
damping(6,3.5,1)    
      
    
def damping_phasespace(yo,k,m):   
    t=linspace(0,50, 1000)
    w0=(k/m)**(1/2)
    r=0.05 #미급감쇠
    q=(r**2-w0**2)**(1/2)
    wd=(w0**2)**(1/2)
    y=exp(-r*t)*(y0*sin(wd*t))
    yprime=-yo*exp(-r*t)*(y0*cos(wd*t)-wd*cos(wd*t))
    
    plt.plot(y,yprime,'g-')
    plt.title('Problem 3-4 Position')
    plt.xlabel('y')
    plt.ylabel('yprime')
    plt.show()

damping_phasespace(6,3.5,1)    
    
    