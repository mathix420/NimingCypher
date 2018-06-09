#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''    Usage:

    >>> from NimingCypher import NCrypter
    >>> crypter = NCrypter("https://key.com")
    >>> encrypted_str = crypter.crypt_text("simple string")
    >>> print(encrypted_str)
'''

from NimingCypher.Chiffrement import ChiffrData, DeChiffrData, GenSum, Dechiffrer, Chiffrer
from NimingCypher.GetWebText import getsite, tri_char
from os import startfile

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
        Sum = GenSum(filebytes.rstrip(b'\x00'))#supprime les bytes nuls de fin de ligne
        fl = ChiffrData(filebytes, self.charlist)
        file.close()
        del filebytes
        return (Sum, fl) #hash sha256 et le fichier chiffré

    def decrypt_file(self, textencrypte, path, open_end=False):
        clear_bytes = DeChiffrData(textencrypte, self.textfromweb, self.charlist)
        if clear_bytes != None:
            sf = open(path, "wb+")
            sf.write(clear_bytes)
            sf.close()
            if open_end == True:
                startfile(path)     #ouvre le fichier
            Sum = GenSum(clear_bytes)
            del clear_bytes
            return Sum
        else:
            return "Erreur lors du déchiffrement !"

    def get_security_level(self):
        c = 0
        for l in self.charlist[1]:
            c += len(l)
        security_lvl = int(c/len(self.charlist[1]))
        if security_lvl < 120:
            return "Poor security : %s" % security_lvl
        elif security_lvl >= 120 and security_lvl < 300:
            return "Medium security : %s" % security_lvl
        elif security_lvl >= 300 and security_lvl < 600:
            return "Pretty good security : %s" % security_lvl
        elif security_lvl >= 600 and security_lvl < 1000:
            return "High security : %s" % security_lvl
        elif security_lvl >= 1000 and security_lvl < 2000:
            return "Verry high security : %s" % security_lvl
        elif security_lvl >= 2000:
            return "Top level security : %s" % security_lvl

    def crypt_text(self, text):
        return ChiffrData(text.encode(), self.charlist)

    def decrypt_text(self, text_bytes):
        return DeChiffrData(text_bytes, self.textfromweb, self.charlist)

    def key_hash(self):
        return self.crypt_text(GenSum(self.textfromweb.encode()))

    def check_hash(self, encrypted_hash):
        return GenSum(self.textfromweb.encode()).encode() == self.decrypt_text(encrypted_hash)

#==================================================================================================================================
