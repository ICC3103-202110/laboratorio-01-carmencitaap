# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 17:31:58 2021

@author: JPA
"""
from numpy import random
num_cards = int(input("With how many cards do you want to play?: ")) #1
won = 1
lost = 1
num_cards2 = num_cards
print("Player 1 starts")

while lost == 1: 
    
    deck = []
    deck1 = []
    for i in range(num_cards):
    #print(num_cards)
        num_cards -= 1
        deck.append(num_cards+1)
        deck1.append(num_cards+1)
        random.shuffle(deck) #2
        random.shuffle(deck1) #2
    #gano = 0
    #print(deck)  #with these prints (both of them) you can see the board, to test the game. 
    #print(deck1)

    p_j1 = 0 #3
    p_j2 = 0 #3
    
    
    hidden_board1 = []
    hidden_board2 = []

    for k in range(num_cards2):
        hidden_board1.append("*")
        hidden_board2.append("*")
    tab = ""
    tab2 = ""
    for a in range(len(hidden_board1)):
        tab += hidden_board1[a]
    for b in range(len(hidden_board2)):
        tab2 += hidden_board2[b]
    
    print(tab)
    print(tab2)
    lost = 0
    #lost = 0
    while won == 1:
        lost = 0
        cd = input("Enter a coordenate to flip one card \n(Pick one from each deck): ") #5
        cd.split(",")
        c1 = int(cd[0])
        c2 = int(cd[2])-1

#flip card 1
        if c1 == 1:
            hidden_board1.pop(c2)
            card1 = int(deck[c2])
            hidden_board1.insert(c2,card1)
    
        elif c1 ==2:
            hidden_board2.pop(c2)
            card1  = int(deck1[c2])
            hidden_board2.insert(c2,card1)
    
#flip card 2
        coord = input("Enter a coordenate to flip another card \n(Pick one from the deck you haven't chosen): ")
        coord.split(",")
        coord1 = int(coord[0])
        coord2 = int(coord[2])-1
        if coord1 == 1:
            hidden_board1.pop(coord2)
            card2 = int(deck[coord2])
            hidden_board1.insert(coord2,card2)

        elif coord1 ==2:
            hidden_board2.pop(coord2)
            card2  = int(deck1[coord2])
            hidden_board2.insert(coord2,card2)

        print(hidden_board1)
        print(hidden_board2)
        if card1 == card2:
            p_j1 += 1
            print("Keep playing! You chose the right pair")
            
            if c1 == 1:
                hidden_board1.pop(c2)
                hidden_board1.insert(c2, "")
            if coord1 == 2:
                hidden_board2.pop(coord2)
                hidden_board2.insert(coord2, "")
                
            end = hidden_board1.count("")
            end1 = hidden_board2.count("")
            won = 1
            print(hidden_board1)
            print(hidden_board2)
            if end == num_cards2 and end == end1:
                print("You've won!")
                lost = 1
                won = 0 

        if card1 != card2:
            print("You've lost, now player 2 gets to play")
        won = 0
        lost = 1
    lost = 0