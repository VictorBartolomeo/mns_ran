# 8. Méthode pour changer l'âge d'une personne.

class Personne:

    def __init__(self, nom, prenom, age): #constructeur pour mon personnage avec les éléments demandés
        self.nom = nom
        self.prenom = prenom
        self.age = age

    def se_presenter(self): #méthode à appeler pour retourner la phrase à partir des éléments appelés au sein de la classe Personne.
        return f"Bonjour, je m'appelle {self.prenom} {self.nom} et j'ai {self.age} ans."

    def anniversaire(self): #on incrémente simplement 1 à son age quand la méthode est appelée.
        self.age += 1

OSS117=Personne("Bonisseur de la Bath", "Hubert", 38) #Je crée mon personnage

for i in range(5): #Le temps va passer plus vite comme ça
    print(OSS117.se_presenter()) #Bonjour Hubert !
    print(OSS117.anniversaire()) #Joyeux anniversaire Hubert !