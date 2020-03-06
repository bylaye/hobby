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

"""
#pour tester ces fonctions on a deux options
1. soite on demande a l'utilisateur de saisir le nombre
dans ce cas on aura a verifier la saisie si le nombre est 
entier et positif ou nul
2. soite on moment d'appeler la fonction on y met aussi le nombre 
mais aussi en veillant a ce que le nombre soit positif ou nul 
"""
# on opte pour l'option 2
print("resultat avec boucle = ",factoriel_boucle(7))
print("resultat avec resursivite = ",factoriel_recursive(6))
