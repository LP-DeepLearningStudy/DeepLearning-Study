import numpy as np

#선형대수학 4.2절 연습문제

def Det(a):
    A=np.array(a)
    B= det(A)
    return B
    
#1
print('#1:',Det([[1,0,3],[5,1,1],[0,1,2]]),'\n')

#2
print('#2:',Det([[0,1,-1],[2,3,-2],[-1,3,0]]),'\n')

#3
print('#3:',Det([[1,-1,0],[-1,0,1],[0,1,-1]]),'\n')

#4
A=np.array([[1,1,0],[1,0,1],[0,1,1]])
print('#4\n:',det(A),'\n')

#5
print('#5\n:',Det([[1,1,0],[1,0,1],[0,1,1]]),'\n')

#6
print('#6\n:',Det([[1,2,3],[4,5,6],[7,8,9]]),'\n')

#7
print('#7\n:',Det([[5,2,2],[-1,1,2],[3,0,0]]),'\n')

#8
print('#8\n:',Det([[1,1,-1],[2,0,1],[3,-2,1]]),'\n')

#9
print('#9\n:',Det([[-4,1,3],[2,-2,4],[1,-1,0]]),'\n')

#14
print('#14\n:',Det([[2,0,3,-1],[1,0,2,2],[0,-1,1,4],[2,0,1,-3]]),'\n')

#26
print('#26\n:',det([[1,1,1],[3,0,-2],[2,2,2]]),'\n')

#57
A=np.array([[1,1],[1,-1]])
b=np.array([[1],[2]])
print('#57:',linalg.solve(A,b),'\n')

#58
A=np.array([[2,-1],[1,3]])
b=np.array([[5],[-1]])
print('#58:',linalg.solve(A,b),'\n')
      
#59
A=np.array([[2,1,3],[0,1,1],[0,0,1]])
b=np.array([[1],[1],[1]])
print('#59:',linalg.solve(A,b),'\n')      

#60
A=np.array([[1,1,-1],[1,1,1],[1,-1,0]])
b=np.array([[1],[2],[3]])
print('#60:',linalg.solve(A,b),'\n')      

#61
A=np.array([[1,1],[1,-1]])
print('#61\n:',inv(A),'\n')

#62
A=np.array([[2,-1],[1,3]])
print('#62\n:',inv(A),'\n')

#63
A=np.array([[2,1,1],[0,1,1],[0,0,1]])
print('#63\n:',inv(A),'\n')
      
#64
A=np.array([[1,1,-1],[1,1,1],[1,-1,0]])
print('#64\n:',inv(A),'\n')














