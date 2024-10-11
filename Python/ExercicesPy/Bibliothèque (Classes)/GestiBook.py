# Note : Dans cette exercice il n’y a ni méthode de classe, ni méthode statique
# ● Créer la classe Livre :
# ○ La classe Livre doit avoir les attributs suivants : titre, auteur,
# annee_de_publication, et disponible (un booléen pour indiquer si le livre est disponible ou non).
# ○ Implémentez une méthode afficher_info() qui affiche les informations sur le livre.
# ○ Implémentez une méthode emprunter() qui change l'état de disponible à False
# si le livre est disponible, sinon affiche un message indiquant que le livre n'est pas
# disponible.
# ○ Implémentez une méthode retourner() qui change l'état de disponible à True.

# ● Créer la classe Bibliotheque :
# ○ La classe Bibliotheque doit avoir une propriété livres qui est une liste d'objets
# Livre
# ○ Implémentez une méthode ajouter_livre() pour ajouter un livre à la bibliothèque.
# ○ Implémentez une méthode afficher_tous_les_livres() qui affiche les informations de tous les livres dans la bibliothèque (qui appel leur méthode afficher_info()).
# ○ Implémentez une méthode compter_livres_disponibles() qui retourne le nombre de livres disponibles dans la bibliothèque.
# ○ Implémentez une méthode rechercher_livre() qui permet de rechercher un livre par son titre.

class Livre:
    def __init__(self, titre,auteur,annee_de_publication, disponible):
        self.titre = titre
        self.auteur = auteur
        self.annee_de_publication = annee_de_publication
        self.disponible = disponible

    def afficher_info(self):
        print(f"Titre: {self.titre}")
        print(f"Auteur: {self.auteur}")
        print(f"Publication: {self.annee_de_publication}")
        print(f"Disponible: {self.disponible}")

    def emprunter(self):
        if self.disponible:
            print(f"Le livre {self.nom} vous a été reservé et n'est plus disponible à la réservation.")
            self.disponible = False

        else:
            print(f"Le livre {self.nom} est déjà emprunté en ce moment. Vous ne pouvez l'emprunter")

    def retourner(self):
        if not self.disponible:
            print(f"Le livre {self.nom} a été remis à la réservation. Merci pour la restitution !")
            self.disponible = True
        else:
            print(f"Le livre {self.nom} est déjà en rayon et disponible.")

class Bibliotheque():
    def __init__(self, liste_livres):
        self.liste_livres = liste_livres

    def ajouter_livre(self):
        self.liste_livres.append(
            (str(input("Titre: ")),
             str(input("Auteur: ")),
             int(input("Publication: ")),
             True))




LOTR=Livre("Le seigneur des Anneaux", "John Reuel Ronald Tolkien", 1962, True)


LOTR.afficher_info()