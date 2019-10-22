#!/bin/python3.6
# Saisie Chaine
# Si int, x3
# sinon print nope

try:
    saisie = float(input("Entrez un chiffre:"))
    print('Resultat:', saisie*3)
except ValueError:
    print("Nope, ce n'est pas un chiffre")
