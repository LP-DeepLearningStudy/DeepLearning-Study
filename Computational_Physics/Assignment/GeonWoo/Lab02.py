# -*- coding: utf-8 -*-

import math
import numpy as np
import matplotlib.pyplot as plt

## Chapter 2 Examples
# Example 2.0.2 - root bisection
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
    return math.cos(2 * x) * math.exp(-x)

# Check fucntion and root
testSet = np.linspace(0,5, num=50)
zeroLine = np.zeros([50,])
vFun01 = np.vectorize(fun01)

# Plotting
plt.title("Ex 2.0.2 Root bisection method")
plt.plot(testSet, vFun01(testSet))
plt.plot(testSet, zeroLine)
plt.show()
print("Example 2.0.2 - root bisection Answer : " + str(root_bisection(fun01, 0, 5)))


# Example 2.0.4 - newton's method
def root_newton(f, df, guess, tolerance=1.0e-6) :
    """
    Uses Newton's method to find a value x near "guess"
    for which f(x) = 0, to within the tolerance given.
    
    It is required to pass this function both f(x) and f`(x).
    """
    x = guess
    dx = 2 * tolerance
    while dx > tolerance :
        x1 = x - f(x)/df(x)
        dx = abs(x - x1)
        x = x1
    return x

def fun02(x) :
    return math.pow(x, 3) + math.pow(x, 2) - 100

def dFun02(x) :
    return 3 * math.pow(x, 2) + 2 * x

# Check fucntion and root
vFun02 = np.vectorize(fun02)
testSet = np.linspace(-6,6, num=50)

# Plotting
plt.title("Ex 2.0.4 newton's method")
plt.plot(testSet, vFun02(testSet))
plt.plot(testSet, zeroLine)
plt.show()
print("Example 2.0.4 - newton's method Answer : " + str(root_newton(fun02, dFun02, 4)))


# Example 2.1.1 - simple integration, inefficient
def int_simple(fn, a, b, N) :
    I = 0
    dx = (b-a) / float(N)
    for j in range(N) :
        x = a + dx * j
        I = I + fn(x) * dx
    return I

def fun03(x) :
    return x

# Check fucntion and root
vFun03 = np.vectorize(fun03)
testSet = np.linspace(0,5, num=50)

# Plotting
print("Example 2.1.1 - simple integration Answer : " + str(int_simple(vFun03, 0, 5, 50)))


 # Example 2.1.3 - simpson's method
def int_simpson(f, dx):
    N = len(f)
    integral = 0.0
     
    for i in range(1, N-1, 2) :
         integral = integral + f[i-1] + 4.0 * f[i] + f[i+1]
         
    integral = integral * dx / 3.0
    
    if (N % 2) == 0 :
        integral = integral + dx * (5.0 * f[-1] + 8.0 * f[-2] - f[-3]) / 12.0
    return integral


 # Example 2.2.1 - derivative
from scipy.misc import derivative
print("Example 2.2.1 - derivative Answer : " + str(derivative(np.sin, np.pi / 2)))
