import pandas as pd
une_liste=[10, np.nan, 12, 16, 8, np.nan, 20]

def fill_list(une_liste):
<<<<<<< Updated upstream

=======
	"""
	une_liste : [10, np.nan, 12, 16, 8, np.nan, 20]
	
	liste_remplie : [10, 11, 12, 16, 8, 14, 20]
	"""
    
>>>>>>> Stashed changes
	#TO DO : Ecrire cette fonction
    s =pd.Series(une_liste)
    s1=s.ffil()
    s2=s.bfill()
    s=(s1+s2)/2
    
    liste_remplie=list(s.values)

	return liste_remplie