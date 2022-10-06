import numpy as np

def fill_list(une_liste):
	"""
	une_liste : [10, np.nan, 12, 16, 8, np.nan, 20]

	liste_remplie : [10, 11, 12, 16, 8, 14, 20]
	"""

	liste_remplie = list()

	for index, item in enumerate(une_liste):
		if not np.isnan(item):
			liste_remplie.append(item)
		else:
			if not index:
				liste_remplie.append(une_liste[index+1])
			elif index == len(une_liste) - 1:
				liste_remplie.append(une_liste[index-1])
			else:
				liste_remplie.append((une_liste[index-1] + une_liste[index+1]) / 2)

	return liste_remplie


print(fill_list([1, 2, np.nan, 4]))
print(fill_list([np.nan, 2, 3, 4]))
print(fill_list([1, 2, 3, np.nan]))
