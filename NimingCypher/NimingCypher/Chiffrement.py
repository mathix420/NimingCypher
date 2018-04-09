#!/usr/bin/env python
# -*- coding: utf-8 -*-

import binascii         #https://docs.python.org/3/library/binascii.html
import hashlib          #https://docs.python.org/fr/3.6/library/hashlib.html
from random import randint as rnd
from NimingCypher.BaseConverter import HexToBase, BaseToHex
import lzma             #utilitaire de compression de données basé sur l'algorithme LZMA

__all__ = []    #utilisé pour n'autoriser l'accès à aucune fonctions
threshold = 10  #utilisé pour définir le nb d'occurrence minimale nécessaire pour l'utilisation dans la base

def chiffrer(Clear_tx,listes_globales):
    liste_char, liste_pos = listes_globales
    final_tx = ""
    pas_trouver = 0
    for ch in Clear_tx: #pour chaque caractères
        if ch in liste_char: #si le carctère est dans la liste des caractères
            idx = liste_char.index(ch)  #on trouve son index dans la liste
            #on récupère la liste de toute les occurences de ce caractère
            #qui possède le même index que la première liste
            lpos = liste_pos[idx]

            #on choisit une de ces occurence aléatoirement
            position = int(lpos[(rnd(0,len(lpos)-1))])

            #on converti la position en hexa et on l'ajoute
            final_tx += str(hex(position))[2:] + " "
        else: #si le caractère n'existe pas dans la liste
            pas_trouver += 1
            final_tx += "0000 "
    print(str(pas_trouver) + ' caractères non trouvés !')
    return(final_tx[:-1]) #retourne tout sauf le dernier caractère " "

def dechiffrer(Encrypted_tx,TextFromWeb):
    OutText = ""
    for ch in Encrypted_tx.split(" "): #pour chaque bloc hexa
        if ch != '': #vérifie que le bloc soit bien existant
            try:
                OutText+=str(TextFromWeb[int(ch,16)]) #retourne le caractère qui correspond à la position en hexa
            except:
                print("Erreur lors du déchiffrement ")
                OutText+= '?'
    return OutText

def GenSum(FileBytes): #génère un hash en sha256 pour la vérification des fichiers appelé sum
    return hashlib.sha256(FileBytes).hexdigest()

def FileToHex(chemin, alphabet, occurlist):
    file = open(chemin,"rb") # r --> read ; b --> byte
    fop = file.read() #stocke le fichier en bytes dans fop
    file.close()
    hx = binascii.hexlify(fop) #on transforme les bytes en hexa
    base = HexToBase(hx, alphabet, occurlist, threshold) #on utilise la base personnalisée pour économiser de la place
    return base

def HexToFile(BaseFile, path, alphabet, occurlist):#inverse de FileToHex
    file = open(path,"wb+") # w --> write ; b --> byte ; + --> créer le fichier si inexistant
    Hx = BaseToHex(BaseFile, alphabet, occurlist, threshold) #base perso vers hexa
    file.write(binascii.unhexlify(Hx))#on écrit le fichier en bytes converti auparavant compressé
    file.close()
    return "Hex to file OK !"

def Compress(data):
    dte = lzma.compress(data)
    return dte

def Decompress(data):
    dtee = lzma.decompress(data)
    return dtee

def ChiffrFile(location, listes): #chiffre le fichier
    liste_char,liste_pos = listes
    hxTxt = FileToHex(location, liste_char, liste_pos)
    chfr = chiffrer(hxTxt, listes)
    compr_tx = Compress(chfr.encode())
    return compr_tx

def DeChiffrFile(textencrypted, textfromweb, listes, path): #dechiffre le fichier
    liste_char,liste_pos = listes
    decompress_tx = Decompress(textencrypted).decode()
    dechTx = dechiffrer(decompress_tx, textfromweb)
    return(HexToFile(dechTx, path, liste_char, liste_pos))
