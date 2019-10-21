#!/bin/python3.6
print ("Saisir une annee:")
annee = input()
int_annee = int(annee)
if (annee%4==0 and annee%100!=0 or annee%400==0):
	print("annee bissextile")
else:
	print("annee non bissextile")
