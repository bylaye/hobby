seconde = input("donner le nombre de seconde ")
seconde = int(seconde)
day = 0
hour = 0
minute = 0

if (seconde >= 0):
	# conversion des secondes => jours: heures: minutes: seconde 
	if (seconde >= 86400):
		day = seconde // 86400
		seconde %= 86400
	if (seconde >= 3600):
		hour = seconde // 3600
		seconde %= 3600
	if (seconde >= 60):
		minute = seconde // 60
		seconde %= 60
	# formatage de l'affichage 
	if len(str(day))<=1:
			day = "0"+str(day)
	if len(str(hour))<=1:
			hour = "0"+str(hour)
	if len(str(minute))<=1:
			minute = "0"+str(minute)
	if len(str(seconde))<=1:
			seconde = "0"+str(seconde)
	print (day,'d:',hour,'h:',minute,'m:',seconde,'s')
else:
	print("donner un nombre postif")
	
