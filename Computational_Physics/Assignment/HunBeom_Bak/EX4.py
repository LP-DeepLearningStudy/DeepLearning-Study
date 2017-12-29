# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 14:15:55 2017

@author: Hunbeom Bak
"""

from pylab import *
from scipy.integrate import odeint
from numpy import *
import matplotlib.pyplot as plt


#Ex4.5.1
N=33333                         #number of steps to take

y=zeros([4])

Lo=1.0                          # unstretched spring length
L = 1.0                         # Initial stretch of spring
vo=0.0                          # initial velocity
theta_o=0.3                     # radians
omega_o=0.0                     # initial angular velocity

y[0]=L
y[1]=vo
y[2]=theta_o
y[3]=omega_o

time = linspace(0,25,N)

k=3.5                           # spring constant (Unit: N/m)
m=0.2                           # mass , (Unit: kg)
g=9.8                           # g , (Unit: m/ s ^2)

def spring_pendulum(y, time):
    g0=y[1]
    g1 =(Lo+y[0])*y[3]*y[3]-k/m*y[0]+g*cos(y[2])
    g2=y[3]
    g3=-(g*sin(y[2])+2.0*y[1]*y[3])/(Lo+y[0])
    
    return array([g0,g1,g2,g3])
answer = odeint(spring_pendulum, y, time)

x_data = (Lo+answer[:,0])*sin(answer[:,2])
y_data = -(Lo+answer[:,0])*cos(answer[:,2])

plt.plot(x_data, y_data, 'b')
plt.xlabel('Horizontial position')
plt.ylabel('Vertical position')
plt.show()
'''
#Example 4.5.2
y=zeros([2])

L = 1.0
g=9.8
beta=1
b=1
omega_o=0.0 

theta=0.3
theta_prime=0


y[0]=theta
y[1]=theta_prime

def pendulum_dam(y, time):
    g0=y[1]
    g1=-g/L*sin(y[0])-b*y[1]+beta*cos(omega*time)
'''    