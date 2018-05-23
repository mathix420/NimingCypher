#!/usr/bin/env python

import binascii         #https://docs.python.org/3/library/binascii.html
import hashlib          #https://docs.python.org/fr/3.6/library/hashlib.html
import lzma             #utilitaire de compression de données basé sur l'algorithme LZMA

from NimingCypher.BaseConverter import IntToBase, BaseToInt
from random import choice

__all__ = []    #utilisé pour n'autoriser l'accès à aucune fonctions
threshold = 10  #utilisé pour définir le nb d'occurrence minimale nécessaire pour l'utilisation dans la base
chunk_size = 64

def intersperse(lst, item):
    result = [item] * (len(lst) * 2 - 1)
    result[0::2] = lst
    return result

def chiffrer(Clear_tx, listes_globales=[]):
    if listes_globales==[]:
        Clear_tx, listes_globales = Clear_tx

    liste_char, liste_pos = listes_globales


    good_ch=[hex(int(choice(liste_pos[liste_char.index(ch)])))[2:] for ch in Clear_tx if ch in liste_char]

    bad_ch=len(Clear_tx)-len(good_ch)

    final_gen=intersperse(good_ch,' ')

    """OLD METHOD - On passe de 10s à 2.2s avec le nv code"""
##    final_tx = ""
##    not_found = 0
##    for ch in Clear_tx: #pour chaque caractères
##        if ch in liste_char: #si le carctère est dans la liste des caractères
##            idx = liste_char.index(ch)  #on trouve son index dans la liste
##            #on récupère la liste de toutes les occurences de ce caractère
##            #qui possède le même index que la première liste
##            lpos = liste_pos[idx]
##
##            #on choisit une de ces occurence aléatoirement
##            position = int(lpos[(rnd(0,len(lpos)-1))])
##
##            #on converti la position en hexa et on l'ajoute
##            final_tx += str(hex(position))[2:] + " "
##        else: #si le caractère n'existe pas dans la liste
##            not_found += 1
##            final_tx += "0000 "
##    print(str(not_found) + ' caractères non trouvés !')
##    return(final_tx[:-1]) #retourne tout sauf le dernier caractère " "
    """END OLD METHOD"""
    print('%s caractères non trouvés !' % (bad_ch))
    return ''.join(final_gen)

def dechiffrer(Encrypted_tx, TextFromWeb):
    OutText = []
    for ch in Encrypted_tx.split(' '): #pour chaque bloc hexa
        if ch != '': #vérifie que le bloc soit bien existant
            try:
                OutText.append(str(TextFromWeb[int(ch,16)])) #retourne le caractère qui correspond à la position en hexa
            except:
                print("Erreur lors du déchiffrement !")
                OutText.append('?')
    return ''.join(OutText)

def GenSum(FileBytes): #génère un hash en sha256 pour la vérification des fichiers appelé sum
    return hashlib.sha256(FileBytes).hexdigest()

def FileToBase(chemin, alphabet, occurlist):
    file = open(chemin,"rb") # r --> read ; b --> byte
    binary_data = file.read() #stock le fichier en bytes dans byte_file
    file.close()
    len_bin = len(binary_data)
    #on transforme les bytes en tableau d'integer de taille chunk_size
    splitted_bin=[int.from_bytes(binary_data[ct:ct+chunk_size], byteorder='little') for ct in range(0, len_bin, chunk_size)]
    #On converti le tableau d'integer en base personnalisée afin d'éconmiser de l'espace
    base = IntToBase(splitted_bin, alphabet, occurlist, threshold)
    return base

def BaseToFile(base_data , path, alphabet, occurlist):#inverse de FileToBase
    try:
        file = open(path,"wb+") # w --> write ; b --> byte ; + --> créer le fichier si inexistant
        int_data = BaseToInt(base_data, alphabet, occurlist, threshold) #base perso vers hexa
        file.write(b''.join([int(i).to_bytes(chunk_size, byteorder='little') for i in int_data]))#on écrit le fichier en bytes converti auparavant compressé
        file.close()
        return True     #aucune erreur
    except:
        return False    #une erreur est survenue

def Compress(data): #compression des données
    comp_data = lzma.compress(data)
    return comp_data

def Decompress(data): #décompression des données
    decomp_data = lzma.decompress(data)
    return decomp_data

def ChiffrFile(location, listes): #chiffre le fichier
    liste_char, liste_pos = listes #liste des caractères présents sur le site et toutes les occurences
    base = FileToBase(location, liste_char, liste_pos) #lis le fichier et le converti en base personalisée
    chfr = chiffrer(base, listes) #on chiffre la base (le texte)
    compr_tx = Compress(chfr.encode()) #on compresse le texte chiffré
    return compr_tx

def DeChiffrFile(textencrypted, textfromweb, listes, path): #dechiffre le fichier
    liste_char,liste_pos = listes #liste des caractères présents sur le site et toutes les occurences
    decompress_tx = Decompress(textencrypted).decode()      #on décompresse et converti les bytes en texte
    dechTx = dechiffrer(decompress_tx, textfromweb)         #on déchiffre
    return BaseToFile(dechTx, path, liste_char, liste_pos)  #on retourne la base transformée en texte
