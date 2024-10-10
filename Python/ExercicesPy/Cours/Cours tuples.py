class PersonnedeLaClasse :
    prenom=""
    nom=""
    age= 18

    def __init__(self, prenom, nom, age):
        self.prenom=prenom
        self.nom=nom
        self.age=age

    def isMajeur(self):
        return self.age >=18

    def bonjour(self, civilite="M.):
        return f"bonjour {civilite}.{self.nom.upper()} {self.prenom.capitalize()},"

prof = PersonnedeLaClasse()
prof.prenom="Franck"
prof.nom="Bansept"
prof.age=37

etudiant = PersonnedeLaClasse()
etudiant.prenom="john"
etudiant.nom="doe"


print(prof.bonjour("M"))

prof= Personne("franck","bansept",37)
etudiant= Personne("john","doe", 25)

print(prof.bonjour("Pr"))