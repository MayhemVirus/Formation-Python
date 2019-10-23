#!/bin/python3.6
#Script avec parametres
#fonction qui renvoie la racine carrée
#fonction qui renvoie la date courante
#fonction qui ecrit une str soit dans un fichier, soit qui print

from math import sqrt
from datetime import datetime
import sys
from argparse import ArgumentParser

def output_to(path, content):
    if path:
        with open(path, "a+") as f:
            f.write(content)
    else:
        print(content)

#definition des paramètre : integer et output
parser = ArgumentParser(description="racine carrée")
parser.add_argument('-i', '--integer', required=True, type=int, nargs=1)
parser.add_argument('-o', '--output')

args = parser.parse_args()
try:
    racine = sqrt(args.integer[0])
    now_date = str(datetime.now())
    result_str = "{date} : {result}\n".format(date=now_date, result=racine)
    output_to(args.output, result_str)
except ValueError:
    print("Integer must be positive")
    sys.exit(-1)

