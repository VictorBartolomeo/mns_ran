#4. Compter les voyelles dans une chaîne

def compter_voyelles(s):
    nb_voyelles=0 #initialise à 0 le nombre de voyelles
    for lettre in s:
        if lettre in "aeiouyAEIOUY": #in cherche si la lettre testée est présente ou non dans la chaine de caractères spécifiée
            nb_voyelles+=1
    return nb_voyelles

phrase="Je suis un cheval, y compris les nuits de pleine lune"
print(compter_voyelles(phrase))