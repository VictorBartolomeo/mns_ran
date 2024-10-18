class Element:
    def __init__(self, valeur):
        self.valeur = valeur
        self.suivant = None


class Liste:
    def __init__(self):
        self.premier_element = None
        self.dernier_element = None

    def ajout(self, valeur_element):
        nouvel_element = Element(valeur_element)
        if self.premier_element is None:
            self.premier_element = nouvel_element
        else:
            self.dernier_element.suivant = nouvel_element

        self.dernier_element = nouvel_element

    def afficher_tout(self):
        avancement = self.premier_element
        while avancement is not None:
            print(avancement.valeur)
            avancement = avancement.suivant


    def supprimer_dernier(self):
        avancement = self.premier_element
        while avancement.suivant.suivant is not None:
            avancement=avancement.suivant
        avancement.suivant = None
        avancement=self.dernier_element

    def supprimer_element(self, index_element_a_supprimer) :
        nb_suppr = self.premier_element
        for occurences in range(index_element_a_supprimer):
            nb_suppr=nb_suppr.suivant
        nb_suppr.suivant=nb_suppr.suivant.suivant

    # retourne une nouvelle liste qui contient les éléments de l'index de début à l'index de fin (ex: 5,8 => renvoie une nouvelle liste avec 5,6,7,8)
    def sous_tableau (self, index_debut, index_fin):

        self.afficher_tout()



ma_meilleur_liste=Liste(3,5)

ma_liste = Liste()

ma_liste.ajout(42)
ma_liste.ajout(12)
ma_liste.ajout(9)
ma_liste.ajout(18)
ma_liste.ajout(14)
ma_liste.ajout(84)
ma_liste.ajout(79)
ma_liste.ajout(44)

ma_liste.supprimer_element(2)
ma_liste.afficher_tout()
