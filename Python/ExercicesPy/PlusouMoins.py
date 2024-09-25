import random
nb_Essai=0
nb_tentative=0
start_again="o"
nb_victoires=0
nb_defaites=0

while start_again is "o" :
    nb_secret = random.randint(1, 100)
    while nb_secret != nb_Essai and nb_tentative<10:
        try: 
            nb_Essai=int(input("Devine un nombre entre 1 et 100 : "))
            nb_tentative+=1
            if nb_Essai>100 or nb_Essai<1 : 
                print("J'ai dis entre 1 et 100...Sans rire ? Ca compte quand même pour un !")
            else :
                if nb_Essai <nb_secret:
                    print("Votre nombre est trop bas")
                elif nb_Essai>nb_secret<=100:
                    print("Votre nombre est trop haut")
                else : 
                    break
                
        except : 
            print("Sans rire ?! J'ai dis un nombre, Bon le prof a dit que ca ne compte pas, t'as eu chaud !")

    if nb_secret==nb_Essai and nb_tentative<8:
        nb_victoires+=1
        nb_secret=0
        print(f"EASY! Vous avez trouvé en {nb_tentative} tentatives, vous êtes à {nb_victoires} W - {nb_defaites} L.")
        try :
            start_again=str(input("Voulez-vous continuer ? o/n\n"))
            if start_again is not "o" : 
                print("Ok bye.") 
                break
            else:
                print("On y retourne !")

        except : 
            print("Sans rire écrit \"o\" ou \"n\" qu'on avance la !")
    elif nb_secret==nb_Essai and nb_tentative>=8:
        nb_victoires+=1
        print(f"CLUTCH! Vous avez trouvé en {nb_tentative} tentatives. (Pas ouf...)")
        try :
            start_again=str(input("Voulez-vous continuer ? o/n\n"))
            if start_again is not "o" :
                print("Ok bye.") 
                break
            else:
                print("On y retourne !")

        except : 
            print("Sans rire écrit \"o\" ou \"n\" qu'on avance la !")

    else : 
        nb_defaites+=1
        print(f"Bon allez on va pas y passer la journée. 10 Tentatives : c'est perdu ! \n Le nombre était {nb_secret} (Oui oui on sait, tu y a pensé, t'étais pas loin... Les cimetières sont pleins de gens \"Pas loin\".")
        try :
            start_again=str(input("Voulez-vous continuer ? o/n\n"))
            if start_again is not "o" : 
                print("Ok bye.") 
                break
            else:
                print("On y retourne !")

        except : 
            print("Sans rire écrit \"o\" ou \"n\" qu'on avance la !")


def bonjour(nom):
    print(f"Bonjour {nom}")

bonjour("Tom")
bonjour("Serge")
bonjour("Didier")