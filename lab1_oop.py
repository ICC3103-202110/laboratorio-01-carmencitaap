# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 17:31:58 2021

@author: JPA
"""
from numpy import random
num_cartas = int(input("¿Con cuántas cartas quieren jugar?: "))
mazo = []
mazo1 = []
for i in range(num_cartas):
    #print(num_cartas)
    num_cartas  -= 1
    mazo.append(num_cartas+1)
    mazo1.append(num_cartas+1)
    random.shuffle(mazo)
    random.shuffle(mazo1)

print(mazo)
print(mazo1)

tablero = [mazo,mazo1]
print(tablero)
print("Comienza jugando el jugador 1")
