#!/bin/python3.6
chaine = "adroit#a3#vroom#b52#colorant#e111"
separation = chaine.split("#")
result = []
for i in separation:
	if i[-1].isdigit():
		result.append(i)
tab = ';'.join(result)
print tab
