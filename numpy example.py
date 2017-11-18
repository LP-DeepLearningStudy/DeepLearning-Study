# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 14:33:30 2017

@author: hukan
"""

import numpy as np #수학 연산, as를 사용하여 축약
import matplotlib.pyplot as plt #그래프 그릴 수 있는 라이브러리

"""
x = np.array([1, 2, 3]) #배열선언
y1 = np.array([2, 4, 7])
y2 = np.array([7, 9, 5])

answer = np.matmul(x,y) #matmul : 내적, add : 더하기, substarct : 빼기

plt.plot(x, y1) #x를 x축, y를 y축으로 그래프 그리기
plt.plot(x, y2)
plt.show()
"""

class Phone :
    
    def __init__(self, brotherNumber) :
        self.myNumber = 1111
        self.myName = '허강민'
        self.myAddress = '인천대'
        self.myBrotherNumber = brotherNumber
    
    def call(self,number) :
        print("전화를 겁니다 - " + str(number)) #str() : 괄호안의 숫자를 문자열로 변환
    
    def answer(self) :
        print("전화를 받습니다")
    
phone01 = Phone(2222)
phone01.call(1515)
phone01.answer()

phone02 = Phone(1212)

if phone01 == phone02 :
    print("두 전화기가 같습니다.")
else :
    print('두 전화기가 다릅니다.')


phone01.myNumber = 1414 #일부 정보 덮어쓰기
phone01.myName = '오효오효'

print(phone01.myNumber)
print(phone01.myName)
print(phone01.myAddress)
print(phone01.myBrotherNumber)
