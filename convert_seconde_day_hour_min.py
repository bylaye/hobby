seconde = input("donner le nombre de seconde ")
seconde = int(seconde)
day = 0
hour = 0
minute = 0

if (seconde > 0):
	if (seconde >= 86400):
		day = seconde // 86400
		seconde %= 86400
	if (seconde >= 3600):
		hour = seconde // 3600
		seconde %= 3600
	if (seconde >= 60):
		minute = seconde // 60
		seconde %= 60
	print (day,' d:',hour,' h:',minute,' m:',seconde,'s')
else:
	print("donner un nombre postif")
