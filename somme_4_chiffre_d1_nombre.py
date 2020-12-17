print("ce programme fait la somme d'un nombre a 4 chiffres donné par l'utilisateur")
while(len(nombre)!=4):
	nombre = input("donner un nombre a 4 chiffre ")
somme = 0
if (len(nombre) == 4):
	for i in range(0,4):
		somme = somme + int(nombre[i])
	print ("la somme de ",nombre[0],"+",nombre[1],"+",nombre[2],"+",nombre[3]," = ",somme)

