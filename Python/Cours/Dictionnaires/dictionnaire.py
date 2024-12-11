#tuple
mon_tuple=("franck","tom","joe")

#liste
ma_liste=["franck","tom","joe"]

#dictionnaire
mon_dictionnaire={"a":"franck","b":"tom","c":"joe"}

for cle, valeur in mon_dictionnaire.items():
    print(f"l'élément {cle} a pour valeur {valeur}")

#ajout d'un élément
mon_dictionnaire["d"]="julie"

#suppression d'un élément
del mon_dictionnaire["a"]

#modification d'un élément
mon_dictionnaire["b"]="julie"

#affichage des éléments
for cle, valeur in mon_dictionnaire.items():
    print(f"l'élément {cle} a pour valeur {valeur}")

class Etudiant:
    def __init__(self, nom, prenom, note):
        self.nom=nom
        self.prenom=prenom
        self.note=note

etudiantA=Etudiant("franck","joe",15)
etudiantB=Etudiant("tom","joe",10)
etudiantC=Etudiant("joe","joe",12)
listeEtudiant=["etudiantA","etudiantB","etudiantC"]

resultatExamen={"admis":[], "recalé":[]}

for etudiant in listeEtudiant:
    if etudiant.note>=10:
        resultatExamen["admis"].append(etudiant)
    else:
        resultatExamen["recalé"].append(etudiant)

for etudiant in resultatExamen["admis"]:
    print(f"{etudiant.nom} {etudiant.prenom} a été admis avec une note de {etudiant.note}")

promo = {"ran4": {"tom":Etudiant("tom","joe",10), "joe":Etudiant("joe","joe",12), "franck":Etudiant("franck","joe",15)},{"ran3": {"tom":Etudiant("tom","joe",10), "joe":Etudiant("joe","joe",12), "franck":Etudiant("franck","joe",15)}}
}

print(promo["ran4"]["tom"].note)
print(promo["ran3"]["tom"].note)