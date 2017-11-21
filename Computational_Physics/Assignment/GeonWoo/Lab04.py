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
    return numpy.array([g0, g1])

 # Example 4.1.2
def euler(y, t, dt, derivs):
    y_next = y + derivs(y,t) * dt
    
