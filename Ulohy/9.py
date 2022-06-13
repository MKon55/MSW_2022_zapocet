#Porovnání výsledků přes Analitickou a Numerickou integraci
import numpy as np
from numpy import *
from scipy import integrate

#Funkce
def polynomial_function(x):
    return x**2 - 2*x + 6

def harmonic_function(x):
    return 2*sin(2*x) 

def logarithm_function(x):
    return log(4*x) + (1/2)

#Metody výpočtu 
def riemann_ctverec(funkce, a, b):
    return integrate.quadrature(funkce, a ,b)

def simpson(funkce, a, b, h=0.01):
    return integrate.simpson(funkce(np.arange(a, b+h, h)), np.arange(a, b+h, h))

def romberg(funkce, a, b):
    return integrate.romberg(funkce, a, b)
 
#Výsledky
print("Polynomická funkce")
print(f"Riemann {riemann_ctverec(polynomial_function, 1, 2)[0]}")
print(f"Simpson {simpson(polynomial_function, 1, 2)}")
print(f"Romberg {romberg(polynomial_function, 1, 2)}")

print("\nHarmonická funkce")
print(f"Riemann {riemann_ctverec(harmonic_function, 1, 2)[0]}")
print(f"Simpson {simpson(harmonic_function, 1, 2)}")
print(f"Romberg {romberg(harmonic_function, 1, 2)}")

print("\nLogaritmická funkce")
print(f"Riemann {riemann_ctverec(logarithm_function, 1, 2)[0]}")
print(f"Simpson {simpson(logarithm_function, 1, 2)}")
print(f"Romberg {romberg(logarithm_function, 1, 2)}")