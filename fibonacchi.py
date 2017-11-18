def fibo(a) :
    
    f = []
    
    for i in range(a) :
        if i == 0 or i == 1 :
            f.append(1)
    
        else :
            f.append(f[i-1]+f[i-2])
    
    return f
    

print(fibo(10))

#http://archi.snu.ac.kr/courses/under/15_spring_computer_concept/fibonacci_explanation.pdf 참조