#2. Jours. (avec le split du bandit)

joursDeLaSemaine=("Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche")
moisDeLAnnee=("Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Aout","Septembre","Octobre","Novembre","Décembre")
date = input('Entrer une date AAAA/MM/JJ: ').split('/')
annee=int(date[0])
mois=int(date[1])
jour=int(date[2])

if date[1]== (1 or 2):
    annee_special=annee-1
    mois_special=mois+12

    N=jour+int((13*mois_special+3)/5)+int(5*annee_special/4)-int(annee_special/100)+int(annee_special/400)
    Nmod=N%7

    print(f"Le {jour} {moisDeLAnnee[mois-1]} {annee} est un {joursDeLaSemaine[Nmod]}")

else:
    N=jour+int((13*mois+3)/5)+int(5*annee/4)-int(annee/100)+int(annee/400)
    Nmod=N%7

    print(f"Le {jour} {moisDeLAnnee[mois-1]} {annee} est un {joursDeLaSemaine[Nmod]}")