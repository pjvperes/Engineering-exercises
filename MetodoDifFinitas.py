import numpy as np
import matplotlib.pyplot as plt

#Inputs
L = 1
T1 = 20
T2 = 10
s = 2
k = 0.1

#Discretização
n = 20
x= np.linspace(0 , L, n)
h = x[1] - x[0]


#Montagem da matriz
diag1 = -2*np.ones(n)
diag2 = np.ones(n-1)

A = np.diag(diag1, 0)
A = A + np.diag(diag2, 1)
A = A + np.diag(diag2, -1)

f = -(s/k) * h**2.0* np.ones(n)

#Condições de contorno
A[0,:] = 0.0
A[0,0] = 1.0
f[0] = T1

A[-1,:] = 0.0
A[-1, -1] = 1.0
f[-1] = T2

#Solucao do sistema linear

T = np.linalg.solve(A, f)

#Plotando o resultado

plt.close('all')
plt.plot(x, T, '-ob')
plt.xlabel ('x')
plt.ylabel('Temperatura')
plt.grid()