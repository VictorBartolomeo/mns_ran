#12. Classe Animal et ses sous-classes Chien et Chat


class Animal:
    def __init__(self, nom):
        self.nom = nom

    def faire_du_bruit(self):
        pass
        # if isinstance(self, Chien):
        #     return f"{self.nom} aboie! Wouf Wouf! 'Comment est votre blanquette ?' (a-t-il dit en chien)."
        # if isinstance(self, Chat):
        #     return f"{self.nom} miaule! Miaou Miaou! 'Je suis le meilleur animal' (a-t-il dit en chat)."
        # if isinstance(self, Animal):
        #     return f"{self.nom} fait un bruit inconnu. Il va peut-être choisir C# ?!"

class Chien(Animal):
    def __init__(self, nom):
        super().__init__(nom)

    def faire_du_bruit(self):
        return f"{self.nom} aboie! Wouf Wouf! 'Comment est votre blanquette ?' (a-t-il dit en chien)."

class Chat(Animal):
    def __init__(self, nom):
        super().__init__(nom)

    def faire_du_bruit(self):
        return f"{self.nom} miaule! Miaou Miaou! 'Je suis le meilleur animal' (a-t-il dit en chat)."


Ada=Chien("Ada")
Mistral=Chat("Mistral")
Njord=Chat("Njord")
# Stephane=Animal("Stephane")
print(Ada.faire_du_bruit())
print(Mistral.faire_du_bruit())
print(Njord.faire_du_bruit())
# print(Stephane.faire_du_bruit())

