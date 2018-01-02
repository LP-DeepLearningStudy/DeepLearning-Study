# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 09:57:10 2017

@author: Hunbeom Bak
"""
import matplotlib.pyplot as plt
import numpy as np

#그래프 그리기 
x= np.array([1,2,3,4,5])
y=x+3
plt.plot(x,y,'rx')                                      #rx는 선이 아니라 점으로만 그린다는 것
plt.title('My first graph')                             #그래프 이름 
plt.xlabel('Time')                                      #x축
plt.ylabel('Distance')                                  #y축    
plt.xlim(0,6)                                           #정의역    
plt.ylim(0,10)                                          #치역
plt.show()

#그래프 그리기(두개)
time = np.linspace(0.0,10.0,100)                        #0부터 10까지 100개
height = np.exp(-time/3)*np.sin(time*3)                     
plt.plot(time,height,'m-^')                             #m-^: 화살표로 칸 표시 m은 보라색?
plt.plot(time,0.3*np.sin(time*3),'g-')                  #g-:그냥 선, g는 초록색
plt.legend(['damped','constant amplitude'],loc='upper right')   #각 그래프마다 이름 붙이고 오른쪽 위에 표시
plt.xlabel('Time(s)')                                           #x축 이름
plt.show()

#Ex0.1.1 Kirchhoff's laws
A= np.array([[-13,2,4],[2,-11,6],[4,6,-15]])
B=np.array([5,-10,5])
print('X=',np.linalg.solve(A,B))                        #AX=B 푼다 


#파일 불러오기
''' 뭔가 문제 있음
frequency, mic1, mic2 = np.loadtxt('microphones.txt', unpack = True)
plt.figure()
plt.plot(frequency, mic1, 'r-', frequency, mic2, 'b-')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude (arbitrary units)')
plt.legend(['Microphone 1', 'Microphone 2'])
'''

