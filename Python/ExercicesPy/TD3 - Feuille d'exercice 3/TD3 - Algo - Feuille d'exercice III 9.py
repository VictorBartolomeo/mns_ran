#9.Une pointe est constituée d’une tête symbolisée par le caractère « _ » et d’une tige symbolisée par le caractère « | ».
# La dimension d’une pointe est la longueur de sa tige, qui correspond au nombre de  caractères « | » présents.
# Ainsi :
# _
# |
# |
# |
# |
# est une pointe de dimension 4.
# L’objectif est d’afficher des pointes d’une dimension donnée.
# Écrire un algorithme affichant p pointes (côte à côte) de dimension d.

d=int(input("Veuillez entrer la dimension de/des flêche.s : "))
p=int(input("Combien de pointes souhaitez-vous ? : "))

for p in range(1,p+1):
    print("_\t", end="")
for d in range (1,d+1):
    print()
    for p in range(1,p+1):
        print("|\t", end="")