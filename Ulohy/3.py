#pass
import numpy as np
from numpy import array
from scipy.linalg import lu

#Gausova eliminační metoda:
def gaus(a):
    x = np.linalg.matrix_rank(a)
    return x

a = array([
    [2,4,4,4],
    [1,2,3,3],
    [1,2,2,2],
    [1,4,3,4]
    ])

pl, u = lu(a, permute_l=True)
print(u)
print(x)

#Jacobiho metoda:
def jacobi(A, b, niteraci, x0=np.ones(len(A))):
    x = x0
    D = np.diag(A)
    L = np.tril(A, k = -1)
    U = np.triu(A, k = 1)
    for i in range(niteraci):
        x = (b - np.matmul((L + U),x))/D
        print("iterace:",i, "x=",x)
    return x

A = array([
    [2,4,4,4],
    [1,2,3,3],
    [1,2,2,2],
    [1,4,3,4]
    ])
b = np.array([11, 13])

x = jacobi(A, b, 10)
print("reseni: ", x)

