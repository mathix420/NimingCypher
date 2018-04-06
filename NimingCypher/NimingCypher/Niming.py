#!/usr/bin/env python
# -*- coding: utf-8 -*-

##    Usage:
##
##    >>> from NimingCypher import NCrypter
##    >>> crypter = NCrypter("https://key.com")
##    >>> encrypted_str = crypter.crypt_text("simple string")
##    >>> print(encrypted_str)

from NimingCypher.Chiffrement import ChiffrFile, DeChiffrFile, GenSum, dechiffrer, chiffrer
from NimingCypher.GetWebText import getsite, tri_char

#Toutes les explications sont dans les fichiers correspondants
#==================================================================================================================================

#utiliser pour autoriser l'accès à ces fonctions uniquement

class NCrypter:

    def __init__(self, Clef):
        self._key = Clef #_key pour rendre le paramètre 'key' privé
        try:
            self.textfromweb = getsite(self._key)
            self.charlist = tri_char(self.textfromweb)
            print('Initialisation terminée !')
        except:
            print('Erreur de connexion !')

    def refresh(self):
        try:
            self.textfromweb = getsite(self._key)
            self.charlist = tri_char(self.textfromweb)
            return True
        except:
            return False

    def crypt_file(self, path):
        file = open(path,"rb")
        filebytes = file.read()
        file.close()
        Sum = GenSum(filebytes)
        del filebytes
        fl = ChiffrFile(path,self.charlist)
        return (Sum, fl) #hash sha256 et le fichier chiffré

    def decrypt_file(self, textencrypte, path):
        from os import startfile
        DeChiffrFile(textencrypte, self.textfromweb, self.charlist, path)
        startfile(path)     #ouvre le fichier
        file = open(path,"rb")    #pour le sum
        filebytes = file.read()
        Sum = GenSum(filebytes)
        file.close()
        del filebytes
        return Sum

    def crypt_text(self, text):
        return chiffrer(text,self.charlist)

    def decrypt_text(self, text):
        return dechiffrer(text, self.textfromweb)

#==================================================================================================================================

if __name__ == '__main__':
    print('''
   _  __ _         _
  / |/ /(_)__ _   (_)___  ___ _
 /    // //  ' \ / // _ \/ _ `/
/_/|_//_//_/_/_//_//_//_/\_, /
                        /___/
Choose an encryption key :
    ''')
Nkey=str(input("~: "))
encrypter = NCrypter(Nkey)
exit = False

while exit == False:
    print('''
    What do you want ?

    1 - Encrypt text
    2 - Decrypt text
    3 - Encrypt file
    4 - Decrypt file

    5 - Quit
    ''')
    choice = int(input("~:"))
    if choice == 1:
        print("Clear text :")
        clear_tx=str(input("~:"))
        cypher_tx = encrypter.crypt_text(clear_tx)
        print(cypher_tx)
    elif choice == 2:
        print("Cypher :")
        cypher_tx=str(input("~:"))
        clear_tx = encrypter.decrypt_text(cypher_tx)
        print(clear_tx)
    elif choice == 3:
        print("Clear file path :")
        clearpath = str(input("~:"))
        print("Encrypted file path :")
        outpath = str(input("~:"))
        sum, encrfile = encrypter.crypt_file(clearpath)
        file = open(outpath,"w+")
        file.write(encrfile)
        file.close()
        print("Sum SHA-256 : %s" % (sum))
    elif choice == 4:
        print("Encrypted file path :")
        encrpath = str(input("~:"))
        print("Clear file path :")
        clearpath = str(input("~:"))
        file = open(encrpath,"r")
        encrfile = file.read()
        file.close()
        sum = encrypter.decrypt_file(encrfile, clearpath)
        del encrfile
        print("Sum SHA-256 : %s" % (sum))
    elif choice == 5:
        exit = True
