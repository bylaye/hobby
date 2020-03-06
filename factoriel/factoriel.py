"""
calcul de factoriel d'un nombre avec l'utilisation 
de fonction recursive et fonction avec boucle for 
Entree : nombre entier 
Sortie : factoriel du nombre entier recu 
"""

# factoriel avec la methode de la recursivite
def factoriel_recursive(nombre):
	if(nombre >= 0):
		if nombre == 0:
			nombre = 1
		else:
			nombre = nombre * factoriel_recursive(nombre-1)
		return nombre


# factoriel par la methode de boucle
def factoriel_boucle(nombre):
	#on a initialise a 1 parce que multiplié par 1 garde le nombre 
	#et aussi le factoriel de 0 est egale a 1
	resultat = 1
	i=1 #valeur qui tourne la boucle
	if nombre != 0:
		for i in range (1, nombre+1):
			resultat = resultat * i
	return resultat 


"""
NB: la methode recursive atteindra ses limites pour une valeur 
superieur a 998
"""
