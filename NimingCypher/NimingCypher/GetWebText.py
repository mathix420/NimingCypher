#!/usr/bin/env python

import urllib.request
from bs4 import BeautifulSoup
from bs4.element import Comment

__all__ = [] #utilisé pour n'autoriser l'accès à aucune fonctions

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']: # si la balise mère est l'une d'elle
        return False                                                                            #retourner False
    if isinstance(element, Comment): #si l'élément est un commentaire
        return False                    #retourner False
    return True                 #sinon retourner True

def html_to_text(data):
    soup = BeautifulSoup(data, 'html.parser') #parse le html
    texts = soup.findAll(text=True) #garde seulement le texte
    visible_texts = filter(tag_visible, texts) #le texte visible
    return u" ".join(t.strip() for t in visible_texts)
    #ajoute le contenu de t (unicode) avec un espace en séparation

def tri_char(texte):
    count= 0
    counter=[]
    liste_char = []
    for ch in texte:                #Pour chaques caractères
        if ch in liste_char:            #Si le caractère est contenu dans la liste de caractères
            pos = liste_char.index(ch)      #obtient l'index du caractère dans la liste de caractères
            counter[pos].append(count)      #ajoute la position du caractère dans la liste des positions
        else:                           #Si le caractère n'existe pas dans la liste
            liste_char.append(ch)           #Ajout du crarctère dans la liste
            counter.append([count])         #Ajout de la position du caractère
        count+=1
    return (liste_char, counter)    #retourn liste de caractères et liste d'occurences

def getsite(url):
    #ouvre et accède au dernier stade de chargement de la page avant de lire son contenu
    html = urllib.request.urlopen(url).read()
    text = html_to_text(html) #parse la page
    return text #retourne le texte
