import numpy as np
from numpy import *
import time

#Tvorba Matice
m = int(input("Zadejte velikost matice: "))
A = np.random.randint(1,100, size = (m,m))
#print(A)
b = np.random.randint(1,100, m)
#print(b)

#Gausova metoda 
def gaus(A,b):
    x = np.linalg.solve(A, b)
    return x

#Jacobiho metoda 
def jacobi(A,b,N=25,x=None):                                                                                                                                                         
    if x is None:
        x = zeros(len(A[0]))                                                                                                                                                                 
    D = diag(A)
    R = A - diagflat(D)                                                                                                                                                                 
    for i in range(N):
        x = (b - dot(R,x)) / D
    return x

#Výpočty + čas pro JACOBI
j_start = time.perf_counter()
jacobi = jacobi(A,b,N=25)
j_end = time.perf_counter()
j= j_end - j_start

#Výpočty + čas pro GAUS
g_start = time.perf_counter()
gaus = gaus(A,b)
g_end = time.perf_counter()
g = g_end - g_start

#Tisk výsledků
print(f"Vyřešená matice pomocí Gausovi metody: {gaus} a čas pro výpočet: {g}")
print(f"Vyřešená matice pomocí Jacobiho metody: {jacobi} a čas pro výpočet: {j}")