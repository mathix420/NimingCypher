#!/usr/bin/env python
# -*- coding: utf-8 -*-
__all__ = []

def GetAlphabet(AlphaList, OccList, threshold):
#demande la liste des caractères trouvés sur la pages et les occurences de ces mêmes caractères
    alphabet = []
    base = ''
    counter = 0
    #initialise les varables utiles
    
    for i in AlphaList:
        if len(OccList[counter]) >= threshold: #si le caractère apparait plus de n fois sur la page web
            alphabet.append(i)          #on ajoute le caractère dans le dictionnaire de caractères
        counter +=1
    return alphabet
    # retourne un nouvel alphabet contenant tout les caractères ayant au moins n occurences avec n=threshold

def HexToBase(Hexa, AlphabetList, OccurList, threshold=10):
    number = int(Hexa,16) #base 16 vers base 10
    alphabet = GetAlphabet(AlphabetList, OccurList, threshold)
    base = ''

#génère une base alphanumérique afin de réduire la taille des fichier et de réduire les répétitions d'occurences
    while number != 0: 
        number,i = divmod(number,len(alphabet)) # divise le nombre par la base et met le reste dans i
        base = alphabet[i] + base               # ajoute a la base le caractère correspondant au code i
    return base

def BaseToHex(base, AlphabetList, OccurList, threshold=10): #inverse de hex to base
    alphabet = GetAlphabet(AlphabetList, OccurList, threshold)
    out = 0
    for i in base: # on multiplie la sortie par la base en ajoutant la valeur correspondant au caractère
        out = out * len(alphabet) + alphabet.index(i) 
    return str(hex(out))[2:] #retourne tout sauf les deux premiers caractères "0x"
