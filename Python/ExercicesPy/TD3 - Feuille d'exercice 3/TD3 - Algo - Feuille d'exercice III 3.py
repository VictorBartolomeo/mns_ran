#3. Le nombre magique.

import random

chiffreMystere=random.randint(1,10)
win=False

while not win:
    try:
        chiffreUser=int(input("Entrez un chiffre entre 1 et 10: "))
        if 0<chiffreUser<11:

            if int(chiffreUser)>chiffreMystere:
                print("Le chiffre mystère est plus petit")
            elif int(chiffreUser)<chiffreMystere:
                print("Le chiffre mystère est plus grand")
            else:
                print("Victoire")
                win=True
        else:
            print("Merci de saisir un chiffre valide")

    except ValueError:
        print("Ceci n'est pas un chiffre, ou celui-ci n'est pas valide")