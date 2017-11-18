import math as mt
import numpy as np
import matplotlib.pyplot as plt

# 1-0
def square():
    sol1 = []
    for i in range(10,21):
        sol1.append(mt.pow(i,2))
    
    return sol1
print(square())

# 1-1
def fibo(a) :
    
    f = []
    
    for i in range(a) :
        if i == 0 or i == 1 :
            f.append(1)
    
        else :
            f.append(f[i-1]+f[i-2])
    
    return f

print(fibo(10))

# 1-2
def projectile(a,b):
    t = []
    h = []
    for j in range(51):
        t.append(0.1*j)
        h.append(a+b*t[j]-0.5*9.8*mt.pow(t[j],2))
    return h
plt.plot(projectile(0,0))


#1-3

#1-4


    
