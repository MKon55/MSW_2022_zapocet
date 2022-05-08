#Porovnání výsledků přes Analitickou a Numerickou integraci

from numpy import *
from scipy.integrate import quad

#Analitická integrace poze pomocí math
def polynomial_analitical_f(lower, upper): 
    return (((upper**3)/3)- (upper**2) + 6*upper) - (((lower**3)/3)- (lower**2) + 6*lower)

def harmonic_analitical_f(lower, upper):
    return (-cos(2*upper)) - (-cos(2*lower))

def logarithm_analitical_f(lower, upper):
    return (upper * log(4*upper) - (upper/2)) - (lower * log(4*lower) - (lower/2))
 
polynomial_analitical = polynomial_analitical_f(1,2)
harmonic_analitical = harmonic_analitical_f(1,2)
logarithm_analitical = logarithm_analitical_f(1,2)

#Numerická integrace pomocí scipy
def polynomial_function(x):
    return x**2 - 2*x + 6

def harmonic_function(x):
    return 2*sin(2*x) 

def logarithm_function(x):
    return log(4*x) + (1/2)

polynomial_numeric = quad(polynomial_function, 1, 2)
harmonic_numeric = quad(harmonic_function, 1, 2)
logarithm_numeric = quad(logarithm_function, 1, 2)

#Výsledky
print(f"Výsledek pomocí analytické metody: {polynomial_analitical}, výsledek pomocí numerické metody: {polynomial_numeric}")
print(f"Výsledek pomocí analytické metody: {harmonic_analitical}, výsledek pomocí numerické metody: {harmonic_numeric}")
print(f"Výsledek pomocí analytické metody: {logarithm_analitical}, výsledek pomocí numerické metody: {logarithm_numeric}")