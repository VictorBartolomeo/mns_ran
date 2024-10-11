#11. Réécrire l’algorithme précédent, mais cette fois-ci on ne connaît pas d’avance combien l’utilisateur
# souhaite saisir de nombres. La saisie des nombres s’arrête lorsque l’utilisateur entre un zéro.

continuer=True
nbUser=int(input("Saisir un nombre : "))
if nbUser==0:
    continuer=False
else:
    nbMax=nbUser

while continuer:
    nbUser=int(input("Encore : "))
    if nbUser==0:
        continuer=False
    if nbUser>nbMax:
        nbMax=nbUser
    else:
        pass

print(f"Le nombre le plus grand que vous ayez saisi est {nbMax}")
