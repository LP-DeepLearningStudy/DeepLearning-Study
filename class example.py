# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 15:26:14 2017

@author: hukan
"""

import numpy as np
import matplotlib.pyplot as plt

class MultiplyPlot :
   
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def multiplyPlotting(self) :
        plt.plot(self.x, self.y)
        
    def showChart(self) :
        plt.show()
        
plot01 = MultiplyPlot(np.array([1, 2, 3]), np.array([4, 5, 6]))
plot01.multiplyPlotting()
plot01.showChart()
