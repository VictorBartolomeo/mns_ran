#1. Dé ASCII
import random

faceDuDe=random.randint(1,6)

if faceDuDe==1:
    print("\n\t0\n")

if faceDuDe==2:
    print("0\n\n\t\t0")

if faceDuDe==3:
    print("0\n\t0\n\t\t0")

if faceDuDe==4:
    print("0\t\t0\n\n0\t\t0")

if faceDuDe==5:
    print("0\t\t0\n\t0\n0\t\t0")

if faceDuDe==6:
    print("0\t0\n0\t0\n0\t0")

#2. Jours.

# joursDeLaSemaine=("Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche")
# moisDeLAnnee=("Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Aout","Septembre","Octobre","Novembre","Décembre")
# date = input('Entrer une date AAAA/MM/JJ: ').split('/')
# annee=int(date[0])
# mois=int(date[1])
# jour=int(date[2])
#
# if date[1]== (1 or 2):
#     annee_special=annee-1
#     mois_special=mois+12
#
#     N=jour+int((13*mois_special+3)/5)+int(5*annee_special/4)-int(annee_special/100)+int(annee_special/400)
#     Nmod=N%7
#
#     print(f"Le {jour} {moisDeLAnnee[mois-1]} {annee} est un {joursDeLaSemaine[Nmod]}")
#
# else:
#     N=jour+int((13*mois+3)/5)+int(5*annee/4)-int(annee/100)+int(annee/400)
#     Nmod=N%7
#
#     print(f"Le {jour} {moisDeLAnnee[mois-1]} {annee} est un {joursDeLaSemaine[Nmod]}")


#3. Le nombre magique.

# import random
#
# chiffreMystere=random.randint(1,10)
# win=False
#
# while not win:
#     try:
#         chiffreUser=int(input("Entrez un chiffre entre 1 et 10"))
#         if 0<chiffreUser<11:
#
#             if int(chiffreUser)>chiffreMystere:
#                 print("Le chiffre mystère est plus petit")
#             elif int(chiffreUser)<chiffreMystere:
#                 print("Le chiffre mystère est plus grand")
#             else:
#                 print("Victoire")
#                 win=True
#         else:
#             print("Merci de saisir un chiffre valide")
#
#     except ValueError:
#         print("Ceci n'est pas un chiffre, ou celui-ci n'est pas valide")


#4. Pas d'une boucle

for i in range(int(input("Borne de départ : ")),int(input("Borne d'arrivée : "))+1,int(input("Pas d'incrément : "))):
    print(i)

#5. 