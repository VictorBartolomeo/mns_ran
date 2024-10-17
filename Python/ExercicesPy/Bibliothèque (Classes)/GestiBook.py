# Note : Dans cette exercice il n’y a ni méthode de classe, ni méthode statique
# ● Créer la classe Livre :
# ○ La classe Livre doit avoir les attributs suivants : titre, auteur,
# annee_de_publication, et disponible (un booléen pour indiquer si le livre est disponible ou non).
# ○ Implémentez une méthode afficher_info() qui affiche les informations sur le livre.
# ○ Implémentez une méthode emprunter() qui change l'état de disponible à False
# si le livre est disponible, sinon affiche un message indiquant que le livre n'est pas
# disponible.
# ○ Implémentez une méthode retourner() qui change l'état de disponible à True.
from idlelib.macosx import hideTkConsole
from logging import PlaceHolder
from tkinter import Menubutton


# ● Créer la classe Bibliotheque :
# ○ La classe Bibliotheque doit avoir une propriété livres qui est une liste d'objets
# Livre
# ○ Implémentez une méthode ajouter_livre() pour ajouter un livre à la bibliothèque.
# ○ Implémentez une méthode afficher_tous_les_livres() qui affiche les informations de tous les livres dans la bibliothèque (qui appel leur méthode afficher_info()).
# ○ Implémentez une méthode compter_livres_disponibles() qui retourne le nombre de livres disponibles dans la bibliothèque.
# ○ Implémentez une méthode rechercher_livre() qui permet de rechercher un livre par son titre.

class Livre:
    def __init__(self, titre, auteur, annee_de_publication, disponible):
        self.titre = titre
        self.auteur = auteur
        self.annee_de_publication = annee_de_publication
        self.disponible = disponible

    def afficher_info(self):
        print(f"Titre: {self.titre}")
        print(f"Auteur: {self.auteur}")
        print(f"Publication: {self.annee_de_publication}")
        print(f"Disponible: {self.disponible}")

    def afficher_titre(self):
        print(self.titre)

    def emprunter(self):
        if self.disponible:
            print(f"Le livre {self.titre} vous a été reservé et n'est plus disponible à la réservation.")
            self.disponible = False
        elif self.disponible == False:
            print(f"Le livre {self.titre} est déjà emprunté en ce moment. Vous ne pouvez l'emprunter")

    def retourner(self):
        if not self.disponible:
            print(f"Le livre {self.titre} a été remis à la réservation. Merci pour la restitution !")
            self.disponible = True
        elif self.disponible:
            print(
                f"Le livre {self.titre} est déjà en rayon. Soit ce livre n'est pas le notre, soit vous nous l'avez volé.")


class Bibliotheque():

    def __init__(self, liste_livres):
        self.liste_livres = liste_livres

    def ajouter_livre(self):
        self.liste_livres.append(Livre(
            str(input("Titre: ")),
            str(input("Auteur: ")),
            int(input("Publication: ")),
            True))

    def comptage_livre(self):
        nbDispo = 0
        for livre in self.liste_livres:
            if livre.disponible:
                nbDispo += 1
        print(
            f"Il y a {len(self.liste_livres)} références dans notre bibliothèque. Parmi lesquels {nbDispo} sont disponibles.")

    def emprunter_livre(self):
        choixEmprunt = str(input("Veuillez écrire le nom du livre à emprunter: "))
        presenceLivre = False
        for livre in self.liste_livres:
            if livre.titre == choixEmprunt:
                livre.emprunter()
                presenceLivre = True
        if presenceLivre == False:
            print(f"Le livre {choixEmprunt} n'existe pas dans la base de donnée.")

    def retourner_livre(self):
        choixRetour = str(input("Veuillez écrire le titre du livre que vous souhaitez restituer: "))
        presenceLivre = False
        for livre in self.liste_livres:
            if livre.titre == choixRetour:
                livre.retourner()
                presenceLivre = True
        if presenceLivre == False:
            print(f"Le livre {choixRetour} n'existe pas dans la base de donnée.")

    def afficher_disponibles(self):
        for livre in self.liste_livres:
            if livre.disponible:
                print(livre.afficher_titre())
            else:
                pass


livre1 = Livre("Le Seigneur des Anneaux", "John Reuel Ronald Tolkien", 1954, True)
livre2 = Livre("Orgueil et Préjugés", "Jane Austen", 1813, False)
livre3 = Livre("1984", "George Orwell", 1949, False)
livre4 = Livre("Harry Potter I", "JK Rowling", 1997, True)

histler_Even = Bibliotheque(liste_livres=[livre1, livre2, livre3, livre4])

choixMenu = int
while choixMenu != 0:
    print("MENU:")
    print("1. Ajouter un livre.")
    print("2. Afficher un ou tous les livres.")
    print("3. Nos références et disponibilités.")
    print("4. Emprunter un livre")
    print("5. Retourner un livre")
    print("\n 0 = QUITTER")

    choixMenu = int(input("\nVeuillez choisir une option :"))

    if choixMenu == 1:
        histler_Even.ajouter_livre()
        for livre in histler_Even.liste_livres:
            livre.afficher_info()
            print("")

    if choixMenu == 2:
        menuRecherche = int(input("Souhaitez vous voir un livre en particulier (1) ou tous les livres (2)? : "))
        if menuRecherche == 1:
            livreRecherche = str(input("Veuillez entrer le titre du livre : "))
            for livre in histler_Even.liste_livres:
                if livre.titre == livreRecherche:
                    print("")
                    livre.afficher_info()
        if menuRecherche == 2:
            for livre in histler_Even.liste_livres:
                livre.afficher_info()
                print("")
    if choixMenu == 3:
        histler_Even.comptage_livre()
        choixRef = str(input("\nVoulez-vous voir les références disponibles ? y/n : "))
        if choixRef == "y":
            histler_Even.afficher_disponibles()
        else:
            pass
    if choixMenu == 4:
        histler_Even.emprunter_livre()
    if choixMenu == 5:
        histler_Even.retourner_livre()
    else:
        pass
