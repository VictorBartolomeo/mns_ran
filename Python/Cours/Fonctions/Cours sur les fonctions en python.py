#Exercice 1:

def aire_rectangle(longueur, largeur):
    return longueur * largeur


print(aire_rectangle(2, 2))


#Exercice 2:

def max_trois_nombres(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c

print(max_trois_nombres(3, 7, 5))

#Exercice 3:

bissextile = False

def annee_bissextile(a):
    if a % 4 == 0 and a % 100 != 0:
        return True
    elif a % 100 == 0 and a % 400 != 0:
        return True
    else:
        return False


if annee_bissextile(2024):
    print("Oui")
else:
    print("Non")

#Exercice 4:

def nb_annee_bissextiles(a, b):
    nombre = 0
    for nbAnnees in range(a, b + 1):
        if annee_bissextile(nbAnnees):
            nombre += 1
    return nombre


print(nb_annee_bissextiles(1900, 2028))


