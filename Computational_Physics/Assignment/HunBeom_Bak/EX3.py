# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 13:28:44 2017

@author: Hunbeom Bak
"""

#3.0 Numpy

from numpy import *
from numpy.linalg import*

M= array([[1,2],[3,4]])

print(M)
print('------------------')

print(M*3)
print('------------------')

print(M+M)
print('------------------')

print(M*M)                          #원소끼리 곱함
print('------------------')

print('dot product\n',dot(M,M))                     #도트 프로덕트
print('------------------')

print('cross product\n',cross(M,M))
print('------------------')         #크로스 프로덕트

print('transpose\n',transpose(M))
print('------------------')

print('역행렬\n',inv(M))
print('from numpy.linalg import * 을 해주어야 한다')
print('------------------')

print('detorminent=',det(M))
print('from numpy.linalg import * 을 해주어야 한다')
print('------------------')

print('아이겐밸류와 아이겐벡터\n',eig(M))
print('from numpy.linalg import * 을 해주어야 한다')
print('------------------')

#EX3.0.1
#여러 경우의 사인값 계산

x= array([pi/6,pi/5,pi/5,pi/3,pi/2])
print('EX3.0.1\n',sin(x))
print('------------------')

#EX3.0.2
#행렬로 연립방정식(Mx=b) 계산

M = array ( [ [ 1 , 3 , -5 , 2 ] , [ 0 , 4 , -2 , 1 ] , [2 , -1 ,3 , -1] , [ 1 , 1 , 1 , 1 ] ] )
b = array ( [ 0 , 6 , 5 , 10 ] )
x = linalg.solve(M, b)
print('Ex3.02\n',x)
print('------------------')

print (arange ( 0 , 1 , 0.25 ))
print('0부터 1까지 0.25 간격으로 생성, 단 마지막 숫자는 포함 ㄴㄴ')

print (arange ( 0 , 1.01 , 0.25 ))
print('0부터 1.01까지 0.25 간격으로 생성, 마지막 숫자가 1.01이므로 1도 포함됨')
print('------------------')

print (logspace( 0 , 3 , 4))
print('10의 0승 부터 10의 3승까지 4개 생성')

print (zeros( [ 2 , 3 ],int ))                          #타입은 int또는 double

print('------------------')

#3.1 Scipy
from scipy.integrate import *

print(quad(sin,0,pi)) #사인을 0부터 파이까지 적분

print(quad(lambda x: exp(-x),0,inf))

#3.2 MatPlotLib
import matplotlib.pyplot as plt

#EX3.2.1
#코사인과 사인을 -pi부터 pi까지 그리기
from pylab import *
x=arange(-pi,pi,pi/100)
plt.plot(x, sin(x),'b-', label='sine')
plt.plot(x, cos(x),'g--', label='cosine')
plt.xlabel('x value')
plt.ylabel('trig function value')
plt.xlim(-pi,pi)
plt.ylim(-1,1)
plt.legend(loc='upper left')
plt.show()

