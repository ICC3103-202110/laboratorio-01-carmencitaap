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
tablero= [mazo,mazo1]
p_j1 = 0 #3
p_j2 = 0 #3

print("Comienza jugando el jugador 1")
tablero_oculto1 = []
tablero_oculto2 = []
fila = []

for k in range(num_cartas2):
    tablero_oculto1.append("*")
    tablero_oculto2.append("*")
#print(tablero_oculto)

coma = ""
comas = ""
for a in range(len(tablero_oculto1)):
    coma += tablero_oculto1[a]
for b in range(len(tablero_oculto2)):
    comas += tablero_oculto2[b]
    #xd += "\n"
print(coma)
print(comas)
coord = input("Ingresa un número para dar vuelta una carta: ") #5
coord.split(",")
coord1 = int(coord[0])
coord2 = int(coord[2])-1

if coord1 == 1:
    tablero_oculto1.pop(coord2)
    carta1 = int(mazo[coord2])
    tablero_oculto1.insert(coord2,carta1)
    
elif coord1 ==2:
    tablero_oculto2.pop(coord2)
    carta2  = int(mazo1[coord2])
    tablero_oculto2.insert(coord2,carta2)

print(coord2)
print(tablero_oculto1)
print(tablero_oculto2)