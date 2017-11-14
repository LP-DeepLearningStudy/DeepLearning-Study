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
M = np.array([])
b = np.array()
x = linalg.solve(M,b)
 
 