#!/bin/python3.6
def nb_mots(ligne):
    ligne_tab = ligne.split(" ")
    return len(ligne_tab)
def nb_total(contenu):
    lignes = contenu.split("\n")
    compteur_ligne = len(lignes)
    compteur_mot = 0
    for ligne in lignes:
        compteur_mot += nb_mots(ligne)
    return (compteur_mot , compteur_ligne)
with open("./texte.txt","r") as f:
    contenu = f.read()
f.close()
print (nb_total(contenu))

def line_count():  
    count = int(0)
    
    file = open('./texte.txt', 'r')
    for i in file.readlines():
        count += 1
    
    file.close()    
    return count

def word_count():  
    count = int(0)
    
    file = open('./texte.txt', 'r')
    for i in file.readlines():
        count += len(i.split())
    
    file.close()
    return count
    
print("There is {} lines".format(line_count()))
print("There is {} words".format(word_count()))