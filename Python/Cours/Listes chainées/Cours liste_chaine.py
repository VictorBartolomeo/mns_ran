from typing import Any


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

    def sous_liste (self, index_debut, index_fin):
        nouvelle_liste=Liste()
        index=0
        avancement=self.premier_element
        while avancement is not None:
            if index_debut <= index <= index_fin:
                nouvelle_liste.ajout(avancement.valeur)
            else:
                pass
            avancement=avancement.suivant
            index+=1
        return nouvelle_liste

    def ajouter_a_chacun_des_elements(self, operation):
        liste_ajout=[]
        avancement = self.premier_element
        while avancement is not None:
            nouvelle_valeur=operation(avancement.valeur)
            liste_ajout.append(nouvelle_valeur)
            avancement = avancement.suivant
        return liste_ajout

    # def donne_inverse(self):
    #     nouvelle_liste = Liste()
    #     avancement = self.premier_element
    #     while avancement is not None:
    #         nouvelle_liste.ajout_au_debut(avancement.valeur)  # Ajoute chaque élément au début de la nouvelle liste
    #         avancement = avancement.suivant
    #     return nouvelle_liste
    #
    # def ajout_au_debut(self, valeur_element):
    #     nouvel_element = Element(valeur_element)
    #     if self.premier_element is None:
    #         self.premier_element = nouvel_element
    #         self.dernier_element = nouvel_element
    #     else:
    #         nouvel_element.suivant = self.premier_element
    #         self.premier_element = nouvel_element


    def afficher_inverse(self, avancement=None):
        if avancement is None:
            avancement=self.premier_element
        if avancement is not None:
            if avancement.suivant is not None:
                self.afficher_inverse(avancement.suivant)
        print(avancement.valeur)

        if avancement is None:
            print(self.premier_element)
        avancement=avancement.suivant

    # def inverse(self):
    #     #franchement j'ai pas trouvé





ma_liste = Liste()

ma_liste.ajout(42)
ma_liste.ajout(12)
ma_liste.ajout(9)
ma_liste.ajout(18)
ma_liste.ajout(14)
ma_liste.ajout(84)
ma_liste.ajout(79)
ma_liste.ajout(44)
