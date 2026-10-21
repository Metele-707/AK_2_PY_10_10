# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 19:27:55 2026

@author: margr / 707-Extreme
Arbeisdkrav 2 PY1010!
"""
# Arbeidskrav 2 - PY1010
#
# Programmet inneholder løsningene på oppgave 1-6.
# Krever NumPy og Matplotlib.
#
# Grafer vises i Spyder sitt Plots-panel.



import matplotlib.pyplot as plt
import math
import numpy as np

# ----------------------------------------
# Oppgave 1
# ----------------------------------------

alder = int(input('Hvilket år er du født? ') )
age_in_2024 = 2024 - alder
print('I 2024 var du',age_in_2024)

# ----------------------------------------
# Oppgave 2
# ----------------------------------------


antall_elever =int(input('Skriv inn antall elever:' ))

pizza = 0.25 * antall_elever 

print(' det trengs',math.ceil(pizza),'pizzaer til klassefesten' )

# ----------------------------------------
# Oppgave 3
# ----------------------------------------

v_grad = float( input('skriv inn gradtallet:' ))
def radian(v_grad):
    return v_grad * np.pi/180
v_rad = radian (v_grad)
print(v_rad ,'er radianet')

# ----------------------------------------
# Oppgave 4A
# ----------------------------------------
 
#Land, Hovedstad, Innbyggertall
land = {
        "Norge": ["Oslo", 0.634],
        "England": ["London", 8.982],
        "Frankrike": ["Paris", 2.161],
        "Italia": ["Roma", 2.873]
        }

# ----------------------------------------
# Oppgave 4B
# ----------------------------------------


chosen_country = (input("hvilket land ønsker du informasjon om?").strip())

print(land[chosen_country][0],'er hovedstaden i', chosen_country,'med', land[chosen_country][1],'millioner innbyggere',)

# ----------------------------------------
# Oppgave 4C
# ----------------------------------------

add_country = (input('What country do you want to add?').strip())
add_capital = input('Whats the capital of the country?').strip()
add_population = float(input('Whats the population?').strip())

land[add_country] = [add_capital, add_population]

print(land)


# ----------------------------------------
# Oppgave 5
# ----------------------------------------


def beregn(a,b):
    # Areal av trekant
    areal_trekant = (a * b) / 2 
    
    # Areal av halvsirkel
    areal_halvsirkel = (np.pi * (a/2)**2) / 2
    
    # totalt areal halvsirkel og trekant
    areal = areal_trekant + areal_halvsirkel
    
    # lengde ytre halvsirkel
    kurve = np.pi * (a/2)
    
    # lengde skråside
    skråside = np.sqrt (a**2 + b**2)
    
    # ytre omkrets
    omkrets = b + skråside + kurve
    
    return areal, omkrets

a = 4
b = 6

areal, omkrets = beregn (a, b)
print('totalt Areal er', areal, 'og omkrets på figur er', omkrets)

# ----------------------------------------
# Oppgave 6
# ----------------------------------------

x= np.linspace(-10, 10, 200)

#f(x) = -x2 - 5
y1 = -x**2 - 5

plt.figure(1)
plt.plot(x, y1)
plt.grid()
