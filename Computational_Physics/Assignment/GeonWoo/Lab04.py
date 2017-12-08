# -*- coding: utf-8 -*-

import math
import numpy as np
from numpy.linalg import *
import matplotlib.pyplot as plt

## Chapter 4 예제 및 문제
 
 # Example 4.1.1
def FreeFall(state, time):
    g0 = state[1]
    g1 = -9.8
    return np.array([g0, g1])

 # Example 4.1.2
def euler(y, t, dt, derivs):
    y_next = y + derivs(y,t) * dt
    return y_next

 # Example 4.1.3
"""
    Euler Method
    F = -mg + kx 풀기 
"""
N = 1000
x0 = 0.0
v0 = 0.0
tau = 3.0
dt = tau/float(N-1)

k = 3.5
m = 0.2
g = 9.8

time = np.linspace(0, tau, N)

y = np.zeros([N,2])
y[0,0] = x0
y[0,1] = v0

def SHO(state, time):
    g0 = state[1]
    g1 = -k/m * state[0] - g
    return np.array([g0, g1])

for j in range(N-1) :
    y[j+1] = euler(y[j], time[j], dt, SHO)
    
xdata = [y[j,0] for j in range(N)]
vdata = [y[j,1] for j in range(N)]

plt.plot(time, xdata)
plt.plot(time, vdata)
plt.xlabel("time")
plt.ylabel("position, velocity")
plt.show()