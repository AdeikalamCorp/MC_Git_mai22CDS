
def fill_list(une_liste):
	"""
	une_liste : [10, np.nan, 12, 16, 8, np.nan, 20]
	
	liste_remplie : [10, 11, 12, 16, 8, 14, 20]
	"""

	#TO DO : Ecrire cette fonction
	une_liste=dropna(une_liste)
	j=0
	for i in range(len(une_liste)):
		liste_remplie=liste_remplie.append(une_liste[i])
		if i ne 
		liste_remplie=liste_remplie.append((une_liste[i]+une_liste[i+1])/2)

	return liste_remplie
