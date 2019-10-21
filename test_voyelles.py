#!/bin/python3.6

def nb_voyelles(saisie):
	voyelles = {"a":0,"e":0,"i":0,"o":0,"u":0,"y":0}
	for lettre in saisie:
		if lettre in voyelles.keys():
			voyelles[lettre] = voyelles[lettre]+1
	return voyelles
print ("Entrez une phrase :")
phrase = input()
print(nb_voyelles(phrase))
