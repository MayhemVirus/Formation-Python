#!/bin/python3.6
import re
def exercice_regex():
    phrase = input("Saisissez votre phrase: ")
    if verif_phrase(phrase):
        groupes = trouver_groupes(phrase)
        print("La phrase est au bon format. Groupes : "+str(groupes))
    else:
        print("La phrase n'est pas au bon format")
    mots = phrase.split(" ")
    for mot in mots:
        if verif_mot(mot):
            continue
        else:
            print ("Nope")
            break
def verif_phrase(phrase):
    mots = phrase.split(" ")
    for mot in mots:
        if verif_mot(mot):
            continue
        else:
            return False
    return True
def trouver_groupes(phrase):
    return re.findall("([0-9]+ \w*)", phrase)
def verif_mot(mot):
    return re.match("[A-Z0-9]\w*",mot)
exercice_regex()

# reg_format = "([A-Z0-9]\w*)"
# re.match("reg_format", phrase)

# reg_group = "([0-9]+ \w*)"
# re.match(reg_format, phrase)
# print (re.match)