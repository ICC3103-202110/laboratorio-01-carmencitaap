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
t_o1 = tablero_oculto1
t_o2 = tablero_oculto2
coma = ""
comas = ""
for a in range(len(tablero_oculto1)):
    coma += tablero_oculto1[a]
for b in range(len(tablero_oculto2)):
    comas += tablero_oculto2[b]
    #xd += "\n"
print(coma)
print(comas)
coord = input("Ingresa una coordenada para dar vuelta una carta: ") #5
coord.split(",")
coord1 = int(coord[0])
coord2 = int(coord[2])-1
#carta1
if coord1 == 1:
    t_o1.pop(coord2)
    carta1 = int(mazo[coord2])
    t_o1.insert(coord2,carta1)
    
elif coord1 ==2:
    t_o2.pop(coord2)
    carta1  = int(mazo1[coord2])
    t_o2.insert(coord2,carta1)
    
print(t_o1)
print(t_o2)

#carta2
coord = input("Ingresa una coordenada para dar vuelta una carta: ")
coord.split(",")
coord1 = int(coord[0])
coord2 = int(coord[2])-1
if coord1 == 1:
    t_o1.pop(coord2)
    carta2 = int(mazo[coord2])
    t_o1.insert(coord2,carta2)
    
elif coord1 ==2:
    t_o2.pop(coord2)
    carta2  = int(mazo1[coord2])
    t_o2.insert(coord2,carta2)

print(t_o1)
print(t_o2)


if carta1 == carta2:
    p_j1 += 1
    print("Continúa jugando!")
    print(tablero_oculto1)
    print(tablero_oculto2)
else:
    print("Ahora juega el jugador 2")

print(p_j1)
    
    
    

    


