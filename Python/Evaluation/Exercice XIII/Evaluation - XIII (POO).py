#Cette version utilise un maximum les objets. Pour les commentaires plus généraux, voir la version avec moins de classes.
# Je pense que le code peut encore être peaufiné. Mais je ne suis pas sûr d'en avoir la capacité.

import random


class Joueur:  #classe pour création de joueurs et leurs actions
    def __init__(self, nom, nb_victoire=0):
        self.nom = nom
        self.defaite = False
        self.nb_victoire = nb_victoire

    def retirer_baton(self): #methode pour le retrait des batons
        while True:
            try:
                retrait_baton = int(input(f"{self.nom}, combien de bâtons souhaitez-vous retirer (1, 2 ou 3) ? "))
                if 1 <= retrait_baton <= 3:
                    return retrait_baton
                else:
                    print("Veuillez saisir un nombre valide entre 1 et 3.")
            except ValueError:
                print("Veuillez saisir un nombre valide.")


class JeuDesBaton: #classe du jeu en lui-même servant à tous les évènements du jeu
    def __init__(self, joueur1, joueur2): #dans le constructeur maintenant, je lui passe ce dont j'ai besoin : des joueurs.
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.joueur_courant, self.joueur_suivant = self.debut_aleatoire()

    def debut_aleatoire(self): #mon début aléatoire en fonction du roll pair ou impair.
        random_start = random.randint(1, 100)
        if random_start % 2 == 0:
            return self.joueur1, self.joueur2
        else:
            return self.joueur2, self.joueur1

    def jouer(self): #méthode du jeu, tours et gestion de la fin incluse.
        jouer = True
        while jouer:
            nb_baton = random.randint(15, 20)
            print(f"Le jeu commence avec {nb_baton} bâtons sur la table.")
            while nb_baton > 0:
                retrait = self.joueur_courant.retirer_baton()
                if retrait > nb_baton:
                    print("Vous essayez de retirer plus de bâtons qu'il n'y en a sur la table.")
                    continue
                nb_baton -= retrait
                if nb_baton <= 0:
                    print(f"{self.joueur_courant.nom}, vous avez perdu.")
                    self.joueur_courant.defaite = True
                    self.joueur_suivant.nb_victoire += 1
                    break
                print(f"Nombre de bâtons restants: {nb_baton}")
                self.joueur_courant, self.joueur_suivant = self.joueur_suivant, self.joueur_courant
            print(f"{self.joueur1.nom} : {self.joueur1.nb_victoire} - {self.joueur2.nom} : {self.joueur2.nb_victoire}")


            #Comme j'ai passé mes joueurs en arguments, je peux gagner une ligne à chaque condition.
            if self.joueur1.defaite:
                self.joueur_courant, self.joueur_suivant = self.joueur1, self.joueur2
                self.joueur1.defaite = False
            elif self.joueur2.defaite:
                self.joueur_courant, self.joueur_suivant = self.joueur2, self.joueur1
                self.joueur2.defaite = False

            while True:
                try:
                    play_again = input("Voulez-vous rejouer ? (Y/n) ")
                    if play_again in ("n", "no"):
                        jouer = False
                        break
                    elif play_again in ("y", "yes", "YES", ""):
                        break
                    else:
                        print("Veuillez saisir 'Y' ou 'n'.")
                except ValueError:
                    print("Veuillez saisir une réponse valide.")


#Je crée mes personnages, je lance le jeu en passant bien mes personnages en arguments puis j'appelle ma boucle principale de jeu
joueur_1 = Joueur("Loktar", 0)
joueur_2 = Joueur("Herr Bramard", 0)
jeu = JeuDesBaton(joueur_1, joueur_2)
jeu.jouer()
