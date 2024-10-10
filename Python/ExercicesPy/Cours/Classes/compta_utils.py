liste_personnage=(
    ("guerrier",100,10,100,50),
    ("magicien",40,100,5,30),
    ("voleur",60,70,20,100),
)

cumul_pv=0
for personnage in liste_personnage:
    cumul_pv+=personnage[1]

print(cumul_pv/len(liste_personnage))