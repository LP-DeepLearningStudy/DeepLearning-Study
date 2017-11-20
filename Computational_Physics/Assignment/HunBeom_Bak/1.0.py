#1.0  10부터 20까지 제곱 나열
def square():
    a=[]
    for i in range(10,21):
        a.append(i**2)   
    return a    
print('10부터 20까지의 제곱',square())