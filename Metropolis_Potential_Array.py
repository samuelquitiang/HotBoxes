import numpy as np
import matplotlib.pyplot as plt

nmax = 50
N = 20
e = True
kb = 1.38e-23
k = kb
T = [10, 100, 500, 1000, 2000]
n = [np.random.randint(1, nmax) for _ in range(N)]
n = np.array(n)
E = [sum(n**2*k)]
t = 1
y = [t]


for T in T:
    while e:
        t+=1
        Ee = 0
        for i in range(N):
            r = np.random.uniform()
            if r > 0.5 and n[i] > 1:
                nc = n[i] - 1
            else:
                nc = n[i] + 1
            Ec = nc**2*k
            Ei = n[i]**2*k
            dE = Ec - Ei
            if dE < 0:
                n[i] = nc
            else:
                r = np.random.uniform()
                W=np.exp(-dE/kb/T)
                if r<=W:
                    n[i] = nc  
            
            Ee += Ei
        E.append(Ee)
        y.append(t)
        if t > 10:
            Emean = sum(E[-10:])/10
            e = abs(Emean-Ee)>1e-25
    print(t,Emean)
    plt.title('Energy in an Array of 20 potential wells')
    plt.ylabel('Energy')
    plt.xlabel('Epoch')
    plt.plot(y,E)
    plt.show()
    