def energy(L1):    
    pi=3.1415
    h=1.05457*10**(-34)
    m=9.109*10**(-31)
    L2=2*L1
    L3=4*L1
    for i in range(1,11):
        for j in range (1,11):
            for k in range (1,11):
                E=((h*pi)**2/(2*m))*((i/L1)**2+(j/L2)**2+(k/L3)**2)
                print(i,",",j,",",k,":",E)
                
energy(1)