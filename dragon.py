#!/usr/bin/env python3
import math
import random

class Animal(object):
    """
    Classe représentant tous les animaux
    """
    def __init__(self, nom):
        self.nom = nom
        self.age = 0
        self.age_max = 42 #magic number a définir plus loin
    
    def vieillir(self):
        #return True si l'animal reste en vie, rtyp:bool
        self.age += 1
        if self.age > self.age_max:
            return False
        self.age += 1
        return True

    def peut_manger(self, animal):
        #isinstance teste le type
        if not isinstance(animal, Animal):
            print("Ca se mange pas ça")
            return False
        return True

class Population:
    def __init__(self):
        self.humains = []
        self.dragons = []
        self.moutons = []
    
    def reproduire_humains(self):
        nb_bebe = int(len(self.humains)/2)
        for i in range(nb_bebe):
            self.humains.append(Humain(nom=Humains.genere_nom()))

    def reproduire_moutons(self):
        nb_agneau = int(len(self.moutons)/2)*2
        for i in range(nb_agneau):
            self.moutons.append(Mouton(nom=Moutons.genere_nom()))

    def passer_une_annee(self):
        #Fait passer une annee
        #returns: true si ce n'est pas fini,False si une liste est vide,et que c'est fini
        self.reproduire_humains()
        self.reproduire_moutons()
        list_animaux = self.humains + self.dragons + self.moutons
        for animal in list_animaux:
            if not animal.vieillir():
                del animal

        for dragon in self.dragons:
            sacrifice = random.choice(self.humains+self.moutons)
            del sacrifice
        if len(self.humains)>0:
            nb_banquet = math.ceil(len(self.humains)/4)
            # _ = je m'en fou,pas de reutilisation donc osef
            for _ in range(0,nb_banquet):
                mouton_cuit = random.choice(self.moutons)
                del mouton_cuit

        if not self.humains:
            print("Oh ils sont tous morts les débiles d'humains")
            return False
        elif not self.moutons:
            print("On a tout mangé ! ")
            return False
        elif not self.dragons:
            print("DOVAHKIIN ! ")
            return False
        return True

    def snap_violent(self):
        self.humains = []
        self.dragons = []
        self.moutons = []

    def jouer(self, nb_dragons, nb_humains, nb_moutons):
        cpt_annees = 0
        for i in range (0,nb_dragons):
            self.dragons.append(Dragons(nom=Dragons.genere_nom()))
        for i in range (0,nb_humains):
            self.humains.append(Humains(nom=Humains.genere_nom()))
        for i in range (0,nb_moutons):
            self.moutons.append(Moutons(nom=Moutons.genere_nom()))
        while self.passer_une_annee():
            cpt_annee += 1
            print("Et une année en plus! Depuis {} ans".format(cpt_annees))

class Dragons(Animal):
    def __init__(self, nom):
        Animal.__init__(self, nom)
        self.age_max = 256
    
    # def peut_manger(self, animal):
    #     if isinstance(animal, Dragons):
    #         print("Je ne mange pas ma famille")
    #         return False
    #     return True
    @staticmethod
    def genere_nom():
        return random.choice(["Alduin","Badass","Tueur","DuFeu"])

class Humains(Animal):
    def __init__(self, nom):
        Animal.__init__(self, nom)
        self.age_max = 50

    def peut_manger(self, animal):
        if not isinstance(animal, Moutons):
            print("Je mange que du mouton")
            return False
        return True

    @staticmethod
    def genere_nom():
        return random.choice(["Robert","Michel","Jeanne","Joseline","Camille","Bitocu"])

class Mouton(Animal):
    def __init__(self, nom):
        Animal.__init__(self, nom)
        self.age_max = 10

    def peut_manger(sel, animal):
        if not isinstance(animal, Animal):
            print("Je ne mange que de l'herbe")
            return False
        return True

    @staticmethod
    def genere_nom():
        return random.choice(["Cotelette","Gigot","Steak","Lasagne","Couscous"])
