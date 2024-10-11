#5. On se propose de calculer la moyenne des notes d’un élève pour certaines matières ; français,  maths, géographie et informatique.
# Pour chacune de ces matières, il faudra saisir un coefficient de pondération compris entre 1 et 10.  Calculez la moyenne en tenant compte des coefficients de pondération.
# Affichez une appréciation :
# Si la moyenne est comprise entre 16 et 20, la mention est « Très bien ».
# Si la moyenne est comprise entre 12 et 16, la mention est « Bien ».
# Si la moyenne est comprise entre 8 et 12, la mention est « Assez bien ».
# Si la moyenne est comprise entre 4 et 8, la mention est « Insuffisant ».
# Si la moyenne est comprise entre 0 et 4, la mention est « Nul ».
# Il faut contrôler que les notes sont comprises entre 0 et 20 et que les coefficients sont compris  entre 1 et 10.

class Matiere :

    def __init__(self, nom):
        self.nom = nom
        self.note=0
        self.coef=0

    def noteValide(self):
        while True:
            try:
                self.note = int(input(f"Saisir la note de la matière : {self.nom} : "))
                if 0 <= self.note <= 20:
                    return self.note
                else:
                    print("Erreur : la note doit être comprise entre 0 et 20.")
            except ValueError:
                print("Erreur")

    def coefValide(self):
        while True:
            try:
                self.coef = int(input(f"Saisir le coefficient de la matière : {self.nom} : "))
                if 1 <= self.coef <= 10:
                    return self.coef
                else:
                    print("Erreur : le coefficient doit être comprise entre 1 et 10.")
            except ValueError:
                print("Erreur")


francais=Matiere("français")
francais.note=francais.noteValide()
francais.coef=francais.coefValide()

maths=Matiere("maths")
maths.note=maths.noteValide()
maths.coef=maths.coefValide()

geographie=Matiere("geographie")
geographie.note=geographie.noteValide()
geographie.coef=geographie.coefValide()

informatique=Matiere("informatique")
informatique.note=informatique.noteValide()
informatique.coef=informatique.coefValide()

moyenne=((francais.note*francais.coef)+(maths.note*maths.coef)+(geographie.note*geographie.coef)+(informatique.note*informatique.coef))/(francais.coef+maths.coef+geographie.coef+informatique.coef)

if 0<moyenne<=4:
    print(f"Avec une moyenne de {round(moyenne)}, vous obtenez la mention \"Nul\"")
elif 5<moyenne<=8:
    print(f"Avec une moyenne de {round(moyenne)}, vous obtenez la mention \"Insuffisant\"")
elif 9<moyenne<=12:
    print(f"Avec une moyenne de {round(moyenne)}, vous obtenez la mention \"Assez bien\"")
elif 12<moyenne<=16:
    print(f"Avec une moyenne de {round(moyenne)}, vous obtenez la mention \"Bien\"")
elif 16<moyenne<=20:
    print(f"Avec une moyenne de {round(moyenne)}, vous obtenez la mention \"Très bien\"")
else:
    print("Valeur en erreur")