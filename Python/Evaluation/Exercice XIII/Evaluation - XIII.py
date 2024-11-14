import random

jouer = True  # va me servir à boucler les games all night long


class Joueur:
    def __init__(self, nom, nb_victoire=0):  # constructeur de mon/mes joueurs,
        # je passe le nb victoire directement à 0 puisque ça ne commencerait pas plus haut,
        # sauf si on faisait une gestion de handicap
        self.nom = nom
        self.defaite = False
        self.nb_victoire = nb_victoire

    def retirer_baton(
            self):  # méthode de retrait des bâtons, je fais le try, except directement dedans, j'aurais pu faire une méthode qui vérifie si le nb est valide autrement.
        while True:
            try:
                retrait_baton = int(input(f"{self.nom}, combien de bâtons souhaitez-vous retirer (1, 2 ou 3) ? "))
                if 1 <= retrait_baton <= 3:
                    return retrait_baton
                else:
                    print("Veuillez saisir un nombre valide")
            except ValueError:
                print("Veuillez saisir un nombre valide")


def debut_aleatoire():  # Randomisation du premier joueur parce que c'est plus rigolo
    global joueur_courant, joueur_suivant  # Portée définie sur globale, sinon je ne peux plus y accéder, du coup ce n'est pas pratique. J'ai appris ça en C# huhu.
    random_start = random.randint(1, 100)
    if random_start % 2 == 0:  # les chiffres pairs font débuter Herr Bramard (j1)
        joueur_courant = joueur_2
        joueur_suivant = joueur_1
    else:  # les chiffres impairs font débuter Loktar (j2)
        joueur_courant = joueur_1
        joueur_suivant = joueur_2


# Création des joueurs et appel du random starter.
joueur_1 = Joueur("Loktar")
joueur_2 = Joueur("Herr Bramard")
#joueur_nb=Joueur(str(input("Veuillez entrer le nom du premier joueur : ")
#Je peux aussi demander le nom des joueurs, mais là, je vais choisir les noms, dans un souci de simplicité.
debut_aleatoire()

# Début
while jouer:  # Boucle de jeu
    nb_baton = random.randint(15, 20)
    print(f"Le jeu commence avec {nb_baton} bâtons sur la table.")
    while nb_baton > 0:
        retrait = joueur_courant.retirer_baton()  # on appelle la méthode pour retirer les batons et comme la vérif est dedans pas de risque d'erreur.

        if retrait > nb_baton:  # vérification si on essaye de retirer plus de bâtons qu'il n'y a sur la table. Déjà ce n'est pas malin mais en plus c'est une défaite assurée.
            print("Vous essayez de retirer plus de bâtons qu'il n'y en a sur la table.")
            continue
        nb_baton -= retrait  # on applique le retrait si toutes les conditions précédents sont passées.

        if nb_baton <= 0:  # vérification si fin de partie. Normalement, ce n'est jamais inférieur avec les check précédents mais ça ne mange pas de pain.
            print(f"{joueur_courant.nom}, vous avez perdu.")
            joueur_courant.defaite = True  # on passe la défaite sur True pour définir plus tard le premier joueur
            joueur_suivant.nb_victoire += 1  # on incrémente la victoire, ca fait toujours du bien un tableau des scores.
            break  # on break la boucle while puisque partie terminée

        print(f"Nombre de bâtons restants: {nb_baton}")
        joueur_courant, joueur_suivant = joueur_suivant, joueur_courant  # on inverse les deux joueurs, vu sur Stack overflow.

    print(
        f"{joueur_1.nom} : {joueur_1.nb_victoire} - {joueur_2.nom} : {joueur_2.nb_victoire}")  # Comme dit, petit score.

    # Tout ca sert à définir qui commence la prochaine partie, en adéquation avec le booléen défaite.
    if joueur_1.defaite:
        joueur_courant = joueur_1
        joueur_suivant = joueur_2
        joueur_1.defaite = False
    elif joueur_2.defaite:
        joueur_courant = joueur_2
        joueur_suivant = joueur_1
        joueur_2.defaite = False

    # Ici on va chercher à savoir si le joueur souhaite rejouer. On va aussi éviter qu'il n'écrive n'importe quoi.
    while True:
        try:
            play_again = str(input("Voulez-vous rejouer ? (Y/n) "))
            #J'aurai pu utiliser la méthode .strip() et .lower() pour contraindre la réponse, mais on va pas surcharger.
            if play_again in ("nN", "non", "NON"):
                jouer = False
                break
            if play_again in ("yY", "yes", "YES", ""):
                break
                # print("Ca fonctionne")
            else:
                print("Veuillez saisir une réponse valide. (Y/n)")
        except ValueError:
            print("Veuillez saisir une réponse valide.")

print("Au revoir, pour rappel {joueur_1.nom} : {joueur_1.nb_victoire} - {joueur_2.nom} : {joueur_2.nb_victoire}")
