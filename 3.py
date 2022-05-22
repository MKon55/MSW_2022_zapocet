#pass
import numpy as np
from numpy import *
import time

#LU dekompozice - zakladni metoda linalg.solve
def gaus(A,b):
    x = np.linalg.solve(A, b)
    return x

#Jacobiho metoda výpočtu matice 
def jacobi(A,b,N=25,x=None):
    # Create an initial guess if needed                                                                                                                                                            
    if x is None:
        x = zeros(len(A[0]))

    # Create a vector of the diagonal elements of A                                                                                                                                                
    # and subtract them from A                                                                                                                                                                     
    D = diag(A)
    R = A - diagflat(D)

    # Iterate for N times                                                                                                                                                                          
    for i in range(N):
        x = (b - dot(R,x)) / D
    return x

# Matice + guess pro Jacobi   
A = array([[2.0,1.0],[5.0,7.0]])
b = array([11.0,13.0])

#Výpočet Jacobi + čas
j_start = time.perf_counter()
jacobi = jacobi(A,b,N=25)
j_end = time.perf_counter()
j= j_end - j_start

#Gaus výpočet + čas 
g_start = time.perf_counter()
gaus = gaus(A,b)
g_end = time.perf_counter()
g = g_end - g_start

#Výsledky 
print(f"Matice levé strany {A}")
print(f"Matice pravé strany {b}")
print(f"Vyřešená matice pomocí Jacobiho metody: {jacobi} a čas pro výpočet: {j}")
print(f"Vyřešená matice pomocí Gausovi metody: {gaus} a čas pro výpočet: {g}")

