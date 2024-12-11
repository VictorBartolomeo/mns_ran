#11. Classe Vehicule et ses sous-classes Velo et Voiture

class Vehicule: #classe pour les véhicules
    def __init__(self, nombre_de_roues, couleur):
        self.nombre_de_roues = nombre_de_roues
        self.couleur = couleur

    def presentation(self): #utilisé pour appeler mes éléments
        if isinstance(self,Voiture): #cible la classe a l'aide de isinstance, je lui passe comme argument ma classe
            return f"La voiture possède {self.nombre_de_portes} portes, est de couleur : {self.couleur} et possède {self.nombre_de_roues} roues."
        if isinstance(self,Velo):
            return f"Le vélo possède {self.nombre_de_roues} roues, est de couleur : {self.couleur}"

class Velo(Vehicule): #je crée la classe Velo en héritage à la classe véhicule (voir le super()...)
    def __init__(self, nombre_de_roues, couleur):
        super().__init__(nombre_de_roues, couleur)

class Voiture(Vehicule):
    def __init__(self, couleur, nombre_de_portes): #je passe un nouvel argument, le nombre de portes
        super().__init__(4, couleur) #je contrains l'héritage du nombre de roues à 4
        self.nombre_de_portes = nombre_de_portes #je déclare mon nombre de portes



velo_a=Velo(2,"bleu")
velo_b=Velo(3,"jaune")
voiture_a=Voiture("rouge",5)

print(velo_a.presentation())
print(velo_b.presentation())
print(voiture_a.presentation())
 #et paf.



