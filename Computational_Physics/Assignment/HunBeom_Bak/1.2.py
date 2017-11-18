#1.2 포탄받아라
import matplotlib.pyplot as plt
def Y(a,b):
    #a:처음위치, b:처음속도
    t=[]
    y=[]
    g=9.8
    for i in range(51):
        t.append(0.1*i)
        y.append(a+b*t[i]-0.5*g*t[i]**2)    
    return y
        
plt.plot(Y(0,0))
plt.show()