#7. Création d'une classe Personne

class Personne:

    def __init__(self, nom, prenom, age): #constructeur pour mon personnage avec les éléments demandés
        self.nom = nom
        self.prenom = prenom
        self.age = age

    def se_presenter(self): #méthode à appeler pour retourner la phrase à partir des éléments appelés au sein de la classe Personne.
        return f"Bonjour, je m'appelle {self.prenom} {self.nom} et j'ai {self.age} ans."

OSS117=Personne("Bonisseur de la Bath", "Hubert", 38) #Je crée mon personnage

print(OSS117.se_presenter()) #Bonjour Hubert !

