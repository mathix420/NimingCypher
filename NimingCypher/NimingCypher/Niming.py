#!/usr/bin/env python

##    Usage:
##
##    >>> from NimingCypher import NCrypter
##    >>> crypter = NCrypter("https://key.com")
##    >>> encrypted_str = crypter.crypt_text("simple string")
##    >>> print(encrypted_str)

from NimingCypher.Chiffrement import ChiffrFile, DeChiffrFile, Compress, Decompress, GenSum, dechiffrer, chiffrer
from NimingCypher.GetWebText import getsite, tri_char

#Toutes les explications sont dans les fichiers correspondants
#==================================================================================================================================
class NCrypter:

    def __init__(self, clef):
        self.result = self.setkey(clef)

    def setkey(self, clef):
        self._key = clef #_key pour rendre le paramètre 'key' privé
        try:
            self.textfromweb = getsite(self._key)
            self.charlist = tri_char(self.textfromweb)
            #Initialisation terminée !
            return True
        except:
            #Erreur de connexion !
            return False

    def crypt_file(self, path):
        file = open(path,"rb")
        filebytes = file.read()
        file.close()
        Sum = GenSum(filebytes)
        del filebytes
        fl = ChiffrFile(path, self.charlist)
        return (Sum, fl) #hash sha256 et le fichier chiffré

    def decrypt_file(self, textencrypte, path, open_end=False):
        from os import startfile
        if DeChiffrFile(textencrypte, self.textfromweb, self.charlist, path):
            if open_end == True:
                startfile(path)     #ouvre le fichier
            file = open(path,"rb")    #pour le sum
            filebytes = file.read()
            Sum = GenSum(filebytes)
            file.close()
            del filebytes
            return Sum
        else:
            return "Erreur lors du déchiffrement !"

    def crypt_text(self, text):
        return chiffrer(text,self.charlist)

    def decrypt_text(self, text):
        return dechiffrer(text, self.textfromweb)

#==================================================================================================================================
