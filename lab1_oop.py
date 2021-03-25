# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 17:31:58 2021

@author: JPA
"""
from numpy import random
num_cartas = int(input("¿Con cuántas cartas quieren jugar?: ")) #1
num_cartas2 = num_cartas
mazo = []
mazo1 = []
for i in range(num_cartas):
    #print(num_cartas)
    num_cartas  -= 1
    mazo.append(num_cartas+1)
    mazo1.append(num_cartas+1)
    random.shuffle(mazo) #2
    random.shuffle(mazo1) #2

print(mazo)
print(mazo1)

tablero = [mazo,mazo1]
print(tablero,"\n")

p_j1 = 0 #3
p_j2 = 0 #3

print("Comienza jugando el jugador 1")
tablero_oculto = []
fila = []

for k in range(num_cartas2):
    fila.append("*")
for l in range(len(tablero)):
    tablero_oculto.append(fila)
print(tablero_oculto)

xd = ""
for a in range(len(tablero_oculto)):
    for b in range(len(tablero_oculto[1])):
        xd += tablero_oculto[a][b]
    xd += "\n"
print(xd)

coord = input("Ingresa una coordenada para dar vuelta una carta: ") #5
coord.split(",")
print(coord)


