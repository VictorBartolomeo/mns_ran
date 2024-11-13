#10. Rectangle aire et périmètre

class Rectangle:

    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def calculer_aire(self):
        return f"L'aire du rectangle est {self.largeur * self.hauteur}."

    def calculer_perimetre(self):
        return f"Le périmètre du rectangle est {2 * (self.largeur + self.hauteur)}."

rectangle_a=Rectangle(15,20)

print(rectangle_a.calculer_aire())
print(rectangle_a.calculer_perimetre())
