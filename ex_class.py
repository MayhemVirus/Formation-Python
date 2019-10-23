#!/usr/bin/env python3

class Plante:
    def __init__(self, racine, couleur):
        self.racine = racine
        self.couleur = couleur

    def couper(self):
        self.racine = None
    
    def changer_couleur(self, couleur):
        sef.couleur = couleur

class Arbre(Plante):
    def __init__(self, racine, couleur_feuillage):
        Plante.__init__(self, racine, couleur_feuillage)
        self.racine = racine
        self.feuillage = feuillage
 #plus besoin car herité de Plante)   
    # def couper(self):
    #     self.racine = None

    def get_racine(self):
        return self.racine

    # def changer_couleur(self,couleur):
    #     self.feuillage = couleur

    def hiver(self):
        self.feuillage = None

class Fleur:
    def __init__(self, racine, petales, couleur):
        self.color = couleur
        self.racine = racine
        self.petales = petales
    
    def couper(self):
        self.racine = None

    def retirer_petales(self, nb_petales):
        self.petales -= nb_petales

    def ajout_petales(self, nb_petales):
        self.petales += nb_petales

    def changer_couleur(self, couleur):
        if couleur in ("Bleue", "Jaune", "Vert"):
            self.color = couleur
fleur = Fleur("Margerite", 25, "Rouge")
print(fleur.racine)
fleur.couper()
print(fleur.racine)
print(fleur.petales)
fleur.retirer_petales(10)
print(fleur.petales)
print(fleur.color)
#ici Orange n'est pas dans le if donc ça ne change pas
fleur.changer_couleur("Orange")
print(fleur.color)