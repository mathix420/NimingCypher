#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib          #https://docs.python.org/fr/3.6/library/hashlib.html
import lzma             #utilitaire de compression de données basé sur l'algorithme LZMA
from NimingCypher.BaseConverter import IntToBase, BaseToInt
from secrets import choice #random but securly

__all__ = []
threshold = 10  #utilisé pour définir le nb d'occurrence minimale nécessaire pour l'utilisation dans la base
chunk_size = 64 #utilisé pour définir la taille des coupes de fichiers

def Intersperse(lst, item):
    result = [item] * (len(lst) * 2 - 1)
    result[0::2] = lst
    return result

def Chiffrer(clear_tx, listes_globales=[]):
    if listes_globales==[]:
        clear_tx, listes_globales = clear_tx
    liste_char, liste_pos = listes_globales

    good_ch=[hex(int(choice(liste_pos[liste_char.index(ch)])))[2:] for ch in clear_tx]

    final_gen=Intersperse(good_ch,' ')
    return ''.join(final_gen)

def Dechiffrer(encrypted_tx, TextFromWeb):
    out = []
    error = False
    for ch in encrypted_tx.split(' '): #pour chaque bloc hexa
        if ch != '': #vérifie que le bloc soit bien existant
            try:
                out.append(str(TextFromWeb[int(ch,16)])) #retourne le caractère qui correspond à la position en hexa
            except:
                error = True
                out.append('?')
    if error:
        print("Erreur lors du déchiffrement !")
    return ''.join(out)

def GenSum(file_bytes): #génère un hash en sha256 pour la vérification des fichiers appelé sum
    return hashlib.sha256(file_bytes).hexdigest()

def BytesToBase(binary_data, alphabet, occurlist):
    len_bin = len(binary_data)
    #on transforme les bytes en tableau d'integer de taille chunk_size
    splitted_bin=[int.from_bytes(binary_data[ct:ct+chunk_size], byteorder='little') for ct in range(0, len_bin, chunk_size)]
    #On converti le tableau d'integer en base personnalisée afin d'éconmiser de l'espace
    base_data = IntToBase(splitted_bin, alphabet, occurlist, threshold)
    return base_data

def BaseToBytes(base_data , alphabet, occurlist):#inverse de FileToBase
    try:
        int_data = BaseToInt(base_data, alphabet, occurlist, threshold) #base perso vers hexa
        #on écrit le fichier en bytes converti auparavant compressé
        return b''.join([int(i).to_bytes(chunk_size, byteorder='little') for i in int_data]).rstrip(b'\x00')
    except:
        return None    #une erreur est survenue

def Compress(data): #compression des données
    comp_data = lzma.compress(data)
    return comp_data

def Decompress(data): #décompression des données
    decomp_data = lzma.decompress(data)
    return decomp_data

def ChiffrData(binary_data, lists): #chiffre le fichier
    liste_char, liste_pos = lists #liste des caractères présents sur le site et toutes les occurences
    base = BytesToBase(binary_data, liste_char, liste_pos) #lis le fichier et le converti en base personalisée
    chfr = Chiffrer(base, lists) #on chiffre la base (le texte)
    if len(chfr) > 1024:
        compr_tx = Compress(chfr.encode()) #on compresse le texte chiffré
        return compr_tx
    else:
        return chfr

def DeChiffrData(encrypted_data, textfromweb, lists): #dechiffre le fichier
    liste_char,liste_pos = lists #liste des caractères présents sur le site et toutes les occurences
    if isinstance(encrypted_data, bytes): #si c'est des bytes
        decompress_tx = Decompress(encrypted_data).decode()      #on décompresse et converti les bytes en texte
    else:
        decompress_tx = encrypted_data
    dechTx = Dechiffrer(decompress_tx, textfromweb)         #on déchiffre
    return BaseToBytes(dechTx, liste_char, liste_pos)  #on retourne la base transformée en texte
