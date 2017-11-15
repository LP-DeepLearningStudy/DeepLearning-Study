# -*- coding: utf-8 -*-

import math
import numpy as np
from numpy.linalg import *
import matplotlib.pyplot as plt

## Chapter 3 예제
 
 # 넘파이 행렬 선언
M = np.array([[1,2],[3,4]])
print(M,"\n")

 # 넘파이 행렬 요소 곱
print(M*3,"\n")

 # 넘파이 행렬 요소 더하기
print(M+M,"\n")

 # 넘파이 행렬 내적
print(np.dot(M,M),"\n")
 
 # 넘파이 행렬 외적
print(np.cross(M,M),"\n")

 # 넘파이 전치행렬 
print(np.transpose(M),"\n")

 # 넘파이 역행렬 - 주의, 역행렬은 numpy.linalg 를 임포트 해야한다.
print(inv(M),"\n")

 # 넘파이 행렬식(디터미넌트)
print(det(M),"\n")

 # 넘파이 고유값과 고유벡터 - 주의, 역행렬은 numpy.linalg 를 임포트 해야한다.
print(eig(M),"\n")

 # Example 3.0.1 넘파이로 사인값 계산하기
x = np.array([math.pi/6, math.pi/5, math.pi/4, math.pi/3, math.pi/2])
print(np.sin(x),"\n")

 # Example 3.0.2 넘파이로 방정식 풀기 
"""
  w + 3x - 5y + 2z = 0
       4x - 2y + z = 6
   2w - x + 3y - z = 5
     w + x + y + z = 10
"""
M = np.array([ [1,3,-5,2], [0,4,-2,1], [2,-1,3,-1], [1,1,1,1] ])
b = np.array([0,6,5,10])
print(linalg.solve(M,b),"\n")
 
 # 넘파이 어레인지 - 0부터 10까지 0.5 씩 증가 배열
print(np.arange(0, 10, 0.5),"\n")

 # 넘파이 린스페이스 - 어레인지와 비슷하나 배열 갯수를 지정
print(np.linspace(0,10,5),"\n") # 배열 갯수는 5개

 # 넘파이 로그스페이스 - 상용로그 스케일
print(np.logspace(0, 3, 5),"\n")

 # 넘파이 영행렬
print(np.zeros([2,3], np.float32),"\n")
 
 # 사이파이 적분
from scipy.integrate import quad
print(quad(np.sin, 0, np.pi),"\n")

 # 사이파이 적분
print(quad(lambda x: np.exp(-x), 0, np.inf),"\n")


 # Problem 3-0 방정식 풀기
def solving_equation():
    M = np.array([[0.2, 1, 1, 1, -1, -1], 
                  [1, 0, 1, -1, 5, 1], 
                  [-1, -3, 2, -1, -1, -1], 
                  [0, 5, -1, 1, 2, 0], 
                  [1, -2, 3, 0.5, 0, 0], 
                  [0.5, -2, -2, -1, 1, -6]])
    b = np.array([24.1312, 46.2798, -61.8372, 31.1466, 51.2106, -5.7008])
    print("Problem 3-0 Answer : ", linalg.solve(M,b), "\n")
solving_equation()


 # Problem 3-1 수직으로 던진 공의 변위
def throwBall():
    v_ = 5
    y_ = 3
    g = -9.8
    t = np.arange(0,1.5, 0.001)
    y= y_ + t*v_ + 0.5 * g * np.power(t,2)
    plt.title("Problem 3-1 thorwBall")
    plt.plot(t, y)
    plt.show()
throwBall()

 