#Chiffrement de cesar 
def cesar_chiffre_nombre (valeur, decalage):
    return (valeur+decalage)%26

def cesar_dechiffre_nombre(valeur, decalage):
    return (valeur-decalage)%26

def cesar_chiffre_message(message,decalage):
    message_crypte = []
    for caractere in message: 
        if caractere == " ":
            caractere_crypte = caractere
        else:
            caractere = caractere.upper() # converti le caractere en majuscule
            nb = ord(caractere) - 65 # converti caractere en nombre
            nb_crypte = cesar_chiffre_nombre(nb, decalage)
            caractere_crypte = chr(nb_crypte+65) # converti nombre en caractere
        message_crypte.append(caractere_crypte)
    message_crypte = "".join(message_crypte)
    return(message_crypte)

def cesar_dechiffre_message (message, decalage):
    message_decrypte = []
    for caractere in message:
        #si le caractere est un espace on ne le change pas 
        if caractere == " ":
            caractere_decrypte = caractere
        else:
            caractere = caractere.upper()
            nb = ord(caractere) - 65 
            nb_decrypte = cesar_dechiffre_nombre(nb, decalage)
            caractere_decrypte = chr(nb_decrypte+65)

        message_decrypte.append(caractere_decrypte)
    message_decrypte = "".join(message_decrypte)
    return (message_decrypte)

