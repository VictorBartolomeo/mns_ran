
TypeForfait = int(input("Type de forfait \n\n1 pour journée\n2 pour saison : "))

Age = int(input("Âge du bénéficiaire : "))

if Age < 12:
    Statut = "Enfant"
elif Age >= 60:
    Statut = "Senior"
else:
    Statut = "Adulte"

if TypeForfait == 1:
    if Statut == "Enfant":
        Tarif = 18.70
    elif Statut == "Senior":
        Tarif = 21.40
    else:
        Tarif = 25.80
elif TypeForfait == 2:
    if Statut == "Enfant":
        Tarif = 300.00
    elif Statut == "Senior":
        Tarif = 340.00
    else:
        Tarif = 510.00
else:
    print("Type de forfait invalide.")
    Tarif = 0

if Tarif > 0:
    print("Statut du bénéficiaire :", Statut)
    print("Tarif du forfait :", Tarif, "€")