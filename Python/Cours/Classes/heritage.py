class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def bonjour(self):
        return f'Bonjour {self.nom} {self.prenom}'
class Etudiant(Personne):
    def __init__(self, nom, prenom, note):
        super().__init__(nom, prenom)
        self.note = note


john=Etudiant("doe","john",20)

print(john.bonjour())