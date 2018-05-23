#!/usr/bin/env python
__all__ = [] #utilisé pour n'autoriser l'accès à aucune fonctions

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

def IntToBase(Number, AlphabetList, OccurList, threshold=10):
    alphabet = GetAlphabet(AlphabetList, OccurList, threshold)
    b_nbr = len(alphabet) - 1
    base, out = [], ''
    delimiter = str(alphabet[-1])

    for trame in Number:
        n = int(trame)
        while n > 0:
            n, r = divmod(n,b_nbr)    # divise le nombre par la base et met le reste dans i
            base.append(alphabet[r])           # ajoute a la base le caractère correspondant au code i
        out += ''.join(base[::-1]) + delimiter
        base=[]
#génère une base alphanumérique afin de réduire la taille des fichier et de réduire les répétitions d'occurences
    return out[:-1]

def BaseToInt(base, AlphabetList, OccurList, threshold=10): #inverse de hex to base
    alphabet = GetAlphabet(AlphabetList, OccurList, threshold)
    b_nbr = len(alphabet) - 1
    delimiter = str(alphabet[-1])
    fin = []
    for trame in base.split(delimiter):
        out = 0
        for i in trame: # on multiplie la sortie par la base en ajoutant la valeur correspondant au caractère
            out = b_nbr * out + alphabet.index(i)
        fin.append(out)
    return fin
