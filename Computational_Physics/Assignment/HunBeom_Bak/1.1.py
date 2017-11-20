#1.1 피보나치 수열
def fibonachi(a):
        b=[]
        for i in range(a):
            if i<=1:
                b.append(1)
            else:
                b.append(b[i-1]+b[i-2])
        return b     

print('피보나치수열:',fibonachi(10))