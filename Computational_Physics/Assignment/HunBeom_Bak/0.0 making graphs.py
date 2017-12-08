# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 16:23:39 2017

@author: Hunbeom Bak
"""

import numpy as np
import matplotlib.pyplot as plt

#0.0 Making graphs
x=np.array([1,2,3,4,5])
y=x*3
print(y)

plt.plot(x,y,'rx')  #그래프 그릴려는 데이터 지정
plt.title('My first graph') #제목
plt.xlabel('Time (fortnight)')
plt.ylabel('Distance (furlongs)')
plt.xlim(0,6)
plt.ylim(0,10)
plt.show()

