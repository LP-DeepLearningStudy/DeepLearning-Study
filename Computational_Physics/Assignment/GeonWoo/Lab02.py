# -*- coding: utf-8 -*-

import math
import numpy as np
import matplotlib.pyplot as plt

# Example 2.0.2
def root_bisection(f, a, b, tolerance=1.0e-6) :
    """
    Use the bisection method to find a value x between a and b
    for which f(x) = 0, to within the tolerance given.
    """
    dx = abs(b-a)
    while dx > tolerance :
        x = (a + b) / 2.0
        if (f(a) * f(x)) < 0 :
            b = x
        else :
            a = x
        dx = abs(b-a)
    return x
    
def fun01(x) :
    return math.cos(x) * math.exp(-x)
# Check fucntion and root
testSet = np.linspace(0,5, num=50)
zeroLine = np.zeros([50,])
vFun01 = np.vectorize(fun01)
# Plotting
plt.title("Root bisection method")
plt.plot(testSet, vFun01(testSet))
plt.plot(testSet, zeroLine)
plt.show()
print(root_bisection(fun01, 0, 5))