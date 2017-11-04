"""
Python basics 1.11 Problems
작성자 : 김건우
"""

import math
import numpy as np
import matplotlib.pyplot as plt
from builtins import int
from numpy import int16, integer

# problem 1-0
def sqareRoot(list) :
    solution = [math.sqrt(x) for x in list]
    print("1-0. answer : \n", solution, "\n")
sqareRoot(range(10,21))

# problem 1-1
def fibonacci(N) :
    temp = [1,1]
    count = 0
    if N > 2 :
        while(len(temp) != N) :
            temp.append(temp[count] + temp[count + 1])
            count += 1
    else :
        print("1-1. answer : N must be greater than 2")
    print("1-1. answer : ", temp, "\n")
fibonacci(12)

# problem 1-2
def projectileMotion() :
    time = np.linspace(0,50)
    projectile = - np.square(time) * 0.5 * 9.8 + time * 1 + 15
    plt.plot(time, projectile)
    plt.title('1-2. answer')
    plt.show()
projectileMotion()

# problem 1-3
def energy(n1, n2, n3) :
    L1 = 2.
    L2 = 2. * L1
    L3 = 4. * L1
    h_bar = 1.054e-34
    pi = 3.141
    m = 9.109e-31
    return math.pow(h_bar, 2) * math.pow(pi, 2) / (2 * m) * ( (math.pow(n1, 2) / math.pow(L1, 2)) + (math.pow(n2, 2) / math.pow(L2, 2)) + (math.pow(n3, 2) / math.pow(L3, 2)) )
def quantumParticle() :
    print("1-3. answer : \n")
    for n1 in range(1,11) :
        for n2 in range(1,11) :
            for n3 in range(1,11) :
                print("n1 : ", n1, " n2 : ", n2, " n3 : ", n3, " Energy : " ,energy(n1,n2,n3))
    
quantumParticle()

# problem 1-4
def sincFunction() :
    x = np.linspace(-5,5)
    y = np.sinc(x)
    plt.plot(x, y)
    plt.title("1-4. sinc function")
    plt.show()
sincFunction()    

# problem 1-5
def triangluarNumber(N) :
    print("1-5. answer : ",N * (N + 1) / 2,"\n")
triangluarNumber(11)

# problem 1-6
def isPrime(N) :
    temp = np.arange(1, N + 1, 1)
    counter = len(temp) - 1
    flag = True
    while flag :    
        if temp[len(temp) - 1] % temp[counter - 1] != 0 :
            if counter == 2 :
                break
            counter -= 1
        else :
            flag = False
            return print("1-6.", N, "is not Prime Number.")
    return print("1-6.", N, "is Prime Number.")
        
    
isPrime(17)