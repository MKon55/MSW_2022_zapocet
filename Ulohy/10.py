# LOTKUV -VOLTERRUV MODEL PREDATOR KORIST
import numpy as np
from matplotlib import pyplot as plt

# metoda Runge -Kutta 4. radu pro funkce bez explicitni casove zavislosti
def rk4(f, y, h):
    k1 = f(y)
    k2 = f(y + (h/2.)*k1)
    k3 = f(y + (h/2.)*k2)
    k4 = f(y + h*k3)
    y = y + (h/6.)*(k1 + 2.*k2 + 2.*k3 + k4)
    return y

# Lotkuv -Volterruv model , r rust, D extinkce ,
# prvni prvek pole korist , druhy predator
def lv_pp(y):
    r = np.array([0.5,0.1]) #argumenty rx a ry => růstové koeficienty
    D = np.array([0.1,0.3]) #hodnoty Dx a Dy => extinční keoficienty
    return np.array([r[0]*y[0] - D[0]*y[0]*y[1],r[1]*y[0]*y[1] - D[1]*y[1]])

# definujeme delku casoveho kroku , pocet kroku , pocatecni velikost populaci
h = 0.01
kroky_max = 9999
krok = 0
cas_pole = np.zeros(kroky_max+1)
korist_pole = np.zeros(kroky_max+1)
predator_pole = np.zeros(kroky_max+1)
y = np.array([8.,2.]) # pocetecní hodnoty 2 => kořist a 1 => predator 
korist_pole[krok] = y[0]
predator_pole[krok] = y[1]

# integrujeme pomoci rk4, ukladame do pole
while krok < kroky_max:
    y = rk4(lv_pp,y,h)
    krok += 1
    korist_pole[krok] = y[0]
    predator_pole[krok] = y[1]
    cas_pole[krok] = krok*h

# vykreslim casovou zavislost
koristplot , = plt.plot(cas_pole ,korist_pole ,'r',linewidth=2,label='korist')
predatorplot , = plt.plot(cas_pole ,predator_pole ,'b',linewidth=2,label='predator')
plt.xlabel('cas')
plt.ylabel('populace')
plt.legend(handles=[koristplot , predatorplot])
plt.show()
