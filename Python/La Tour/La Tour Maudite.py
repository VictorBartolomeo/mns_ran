import random
def probabilite(chance):
    return random.random() < chance

#1. Début de l'aventure
reussite_mecanisme=False
attaque=0
defense=0

print("Dès le début de ton aventure, tu trouves trois armes différentes dans ta cellule :")
print("Choix 1: Une épée rouillée.")
print("Choix 2: Une baguette magique abîmée.")
print("Choix 3: Un bouclier en bois.")

choix_arme=int(input("Veuillez choisir une arme: "))

if choix_arme==1:
    print("\nTu as choisi l'épée")
    attaque+=10
    defense+=2
elif choix_arme==2:
    print("\nTu as choisi la baguette")
    attaque+=6
    defense+=5
elif choix_arme==3:
    print("\nTu as choisi la bouclier")
    attaque+=3
    defense+=8

#2. Premier étage - La porte verrouillées :

print("Après avoir pris ton arme, tu montes au premier étage et trouves une porte fermée.\nTrois mécanismes sont disponibles pour l'ouvrir :")
print("\n\tMécanisme 1: Résoudre une énigme mathématique.")
print("\tMécanisme 2: Forcer la porte avec ton arme.")
print("\tMécanisme 3: Tenter de trouver une clé cachée dans la pièce.")

choix_mecanisme=int(input("Quel mécanisme souhaitez vous choisir ? : "))

    #Vérification des mécanismes
    #Cas du mécanisme 1
if choix_mecanisme==1:
    enigme=int(input("Combien font 8+3*2 ? : "))
    if enigme==8+3*2:
        print("\nExact! Le passage s'ouvre.")
        reussite_mecanisme=True
    else:
        print("\nVous répondez mal à l'énigme, le mécanisme reste de marbre.")
        reussite_mecanisme=False

    #Cas du mécanisme 2
elif choix_mecanisme==2:
    if choix_arme==1:
        if probabilite(50/100):
            print("\nVous frappez aussi fort que possible, le mécanisme s'ouvre")
            reussite_mecanisme=True
        else:
            print("\nVous frappez aussi fort que possible, malheureusement ca ne suffira pas.")
            reussite_mecanisme=False
    elif choix_arme==2:
        print("\nVous frappez aussi fort que possible avec votre bouclier. Ce n'est pas très efficace. Le mécanisme ne s'ouvrira pas.")
        reussite_mecanisme=False
    elif choix_arme==3:
        if probabilite(30/100):
            print("\nVous lancez un puissant sort et le mécanisme entre en résonnance. Il s'ouvre devant votre puissance.")
            reussite_mecanisme=True
        else:
            print("\nVous rassemblez les arcanes et lancez le sort de guérison des ongles incarnés. Le mécanisme n'en a que faire.")
            reussite_mecanisme=False

    #Cas du mécanisme 3:
elif choix_mecanisme==3:
    if probabilite(40/100):
        print("\nVous cherchez la clef et la trouvez coincée entre deux dalles. L'aventure continue!")
        reussite_mecanisme=True
    else:
        print("\nVous cherchez la clefs des jours durant, puis vous effondrez. Épuisé. L'aventure se termine.")
        reussite_mecanisme=False

#3. Deuxième étage :

if reussite_mecanisme:
    reussite_garde=False
    print("\nVous arrivez au deuxième étage et faites face à un garde spectral.")
    garde_spectral_atk=8
    garde_spectral_def=6
    if attaque>garde_spectral_atk:
        print("Grace à votre épée, vous blessez le garde et réussissez à passer au prochain étage!")
        reussite_garde=True
    elif defense>garde_spectral_atk:
        print("Le garde ne peut pas te blesser, il faut trouver une autre solution !")
        fuite=str(input("Souhaitez-vous fuir ? o/n : "))
        if fuite is "o":
            reussite_garde=True
            print("Vous prenez la fuite!")
        else:
            reussite_garde=False
            print("Vous ne prenez pas la fuite, combattez jusqu'à ce que vous vos dernières forces vous quittent.")
    elif not attaque>garde_spectral_atk and not defense>garde_spectral_def:
        print("Tu perds le combat, l'aventure prend fin ici.")

        ##Ajouter les conditions complexes##

#4. Troisième étage - La Salle du miroir magique:

if reussite_mecanisme and reussite_garde:
    reussite_miroir=False
    print("\nVous arrivez dans une salle sombre dans laquelle trône un miroir.")
    print("A votre grande surprise, ce dernier prend la parole et vous pose une énigme :\n\t\"Je suis toujours devant toi, mais tu ne peux jamais me dépasser. Qui suis-je ?\"")
    print("\tRéponse 1: \"Le futur\"")
    print("\tRéponse 2: \"Le chemin\"")
    print("\tRéponse 3: \"Ton ombre\"")
    reponse_miroir=int(input())
    if reponse_miroir==1:
        print("Le miroir vous montre un futur dangereux, vous choisissez de faire demi-tour. Fin de l'aventure.")
        reussite_miroir=False
    elif reponse_miroir==2:
        print("Le miroir s'ouvre, vous pouvez passer à travers.")
        reussite_miroir=True
    elif reponse_miroir==3:
        for loop in range(30):
            print("Le miroir vous emprisonne dans une boucle temporelle, l'aventure se termine ici.")
        reussite_miroir=False

#5. Dernier étage – Le gardien du sommet :

reussite_porte=False
if reussite_mecanisme and reussite_garde and reussite_miroir:
    print("Au sommet de la tour, tu fais face au Gardien du Sommet, un puissant sorcier qui te lance un défi.")
    print("Il vous demande de choisir une porte parmi trois :")
    print("\tPorte 1: Une porte enflammée.")
    print("\tPorte 2: Une porte gelée.")
    print("\tPorte 3: Une porte d'ombre.")
    choix_porte=int(input("Quelle porte souhaitez vous choisir ? : "))

    if choix_porte==1:
        if choix_arme==1:
            print("Grâce au pouvoir de l'épée, vous pouvez traverser la porte enflammée sans vous blesser. Vous vous échappez de la tour.")
            reussite_porte=True
        else:
            print("Vous êtes emprisonné pour toujours dans la tour.")
            reussite_porte=False
    elif choix_porte==2:
        if choix_arme==3:
            print("Vous pouvez vous protéger du froid grâce à votre bouclier. Vous vous échappez de la tour.")
            reussite_porte=True
        else:
            print("Vous êtes emprisonné pour toujours dans la tour.")
            reussite_porte=False
    elif choix_porte==3:
        if choix_arme==2:
            print("Grâce aux pouvoirs de la baguette, vous arrivez à dissiper l'ombre et traverser la porte pour vous échapper de la tour.")
            reussite_porte=True
        else:
            print("Vous êtes emprisonné pour toujours dans la tour.")
            reussite_porte=False



