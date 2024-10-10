#1. Dé ASCII
# import random
#
# faceDuDe=random.randint(1,6)
#
# if faceDuDe==1:
#     print("\n\t0\n")
#
# if faceDuDe==2:
#     print("0\n\n\t\t0")
#
# if faceDuDe==3:
#     print("0\n\t0\n\t\t0")
#
# if faceDuDe==4:
#     print("0\t\t0\n\n0\t\t0")
#
# if faceDuDe==5:
#     print("0\t\t0\n\t0\n0\t\t0")
#
# if faceDuDe==6:
#     print("0\t0\n0\t0\n0\t0")

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

# for i in range(int(input("Borne de départ : ")),int(input("Borne d'arrivée : "))+1,int(input("Pas d'incrément : "))):
#     print(i)

#5. On se propose de calculer la moyenne des notes d’un élève pour certaines matières ; français,  maths, géographie et informatique.
# Pour chacune de ces matières, il faudra saisir un coefficient de pondération compris entre 1 et 10.  Calculez la moyenne en tenant compte des coefficients de pondération.
# Affichez une appréciation :
# Si la moyenne est comprise entre 16 et 20, la mention est « Très bien ».
# Si la moyenne est comprise entre 12 et 16, la mention est « Bien ».
# Si la moyenne est comprise entre 8 et 12, la mention est « Assez bien ».
# Si la moyenne est comprise entre 4 et 8, la mention est « Insuffisant ».
# Si la moyenne est comprise entre 0 et 4, la mention est « Nul ».
# Il faut contrôler que les notes sont comprises entre 0 et 20 et que les coefficients sont compris  entre 1 et 10.

# erreur=False
# class Matiere :
#     note=""
#     coef=""
#
# def erreurSaisie(self,note,coef):
#     self.note=note
#     self.coef=coef
#     if self.note in range (1,21) and self.coef in range(1,11):
#         return self.note
#         return self.coef
#         erreur=False
#     else:
#         erreur=True
#         print("Erreur de saisie")
#
# while erreur==False:
# français=Matiere()
# français.note=int(input("Saisir la note de français: "))
# français.coef=int(input("Saisir le coefficient du français: "))
#
# if not erreur:
#     maths=Matiere()
#     maths.note=int(input("Saisir la note de maths: "))
#     maths.coef=int(input("Saisir le coefficient du maths: "))
# else:
#     print("ici")
#
# geographie=Matiere()
# geographie.note=int(input("Saisir la note de geographie: "))
# geographie.coef=int(input("Saisir le coefficient du geographie: "))
#
# informatique=Matiere()
# informatique.note=int(input("Saisir la note de informatique: "))
# informatique.coef=int(input("Saisir le coefficient du informatique: "))
#
#
#
# moyenne=((français.note*français.coef)+(maths.note*maths.coef)+(geographie.note*geographie.coef)+(informatique.note*informatique.coef))/(français.coef+maths.coef+geographie.coef+informatique.coef)
#
# if 0<moyenne<=4:
#     print(f"Avec une moyenne de {moyenne}, vous obtenez la mention \"Nul\"")
# if 5<moyenne<=8:
#     print(f"Avec une moyenne de {moyenne} vous obtenez la mention \"Insuffisant\"")
# if 9<moyenne<=12:
#     print(f"Avec une moyenne de {moyenne} vous obtenez la mention \"Assez bien\"")
# if 12<moyenne<=16:
#     print(f"Avec une moyenne de {moyenne} vous obtenez la mention \"Bien\"")
# if 16<moyenne<=20:
#     print(f"Avec une moyenne de {moyenne} vous obtenez la mention \"Très bien\"")
# else:
#     print("valeur en erreur")


#6.Écrivez un algorithme qui convertisse un nombre de la base 10 vers la base 2 (en binaire).  Le principe utilisé est celui de la division entière.
# Prenons le chiffre 19 pour le convertir en base 2.
# La division entière de 19 par 2 donne un quotient de 9 et un reste de 1.
# La division entière de 9 par 2 donne un quotient de 4 et un reste de 1.
# Plaçons les restes dans l’ordre inverse de leur apparition, nous obtenons « 11 ».  La division de 4 par 2 donne un quotient de 2 et un reste de 0.
# L’accumulation des restes donne « 011 ».
# La division de 2 par 2 donne un quotient de 1 et un reste de 0.
# L’accumulation des restes donne « 0011 ».
# La division de 1 par 2 donne un quotient de 0 et un reste de 1.
# L’accumulation des restes donne « 10011 ».
# La conversion s’arrête là et le chiffre 19 converti en base 2 est « 10011 »

# nbConvert=int(input("Veuillez entrer un nombre à convertir : "))
# decimal=nbConvert
# bin=""
#
# if nbConvert ==0:
#     bin="0"
# else:
#     while decimal > 0:
#         reste= decimal % 2
#         bin=str(reste)+bin
#         decimal//=2
#
# print(f"{nbConvert} en binaire est {bin}")

#7. Écrivez l’algorithme qui affiche à l’écran les lignes suivantes :
# 10 11 12 13 14 15
# 20 21 22 23 24 25
# 30 31 32 33 34 35
# 40 41 42 43 44 45
# 50 51 52 53 54 55
# i=0
# for i in range (1,6):
#     for n in range (1,6):
#         print(f"{i}{n} ", end="")
#     print("")

#8.L’élève placé au fond de la classe, près du radiateur, est le meilleur de la classe.
# Pour tuer le temps,  il décide de plier une feuille en deux puis en deux, puis… en deux, puis…
# Écrivez un algorithme  qui calcule l’épaisseur du pliage final à partir du nombre de plis et de l’épaisseur initiale de la  feuille.

# import math (finalement non...)
# epaisseurInitiale=int(input("Veuillez entrer l'épaisseur de la page en mm: "))
# epaisseurFinale=epaisseurInitiale
# nbPliages=int(input("Veuillez entrer le nombre de pliages effectué sur la feuille : "))
#
# for nbPliages in range(1,nbPliages+1):
#     epaisseurFinale+=epaisseurFinale
#
# print(f"Avec une épaisseur de {epaisseurInitiale}mm et {nbPliages} pliages en deux, il en résulte une épaisseur de {epaisseurFinale}mm")

#9.Une pointe est constituée d’une tête symbolisée par le caractère « _ » et d’une tige symbolisée par le caractère « | ».
# La dimension d’une pointe est la longueur de sa tige, qui correspond au nombre de  caractères « | » présents.
# Ainsi :
# _
# |
# |
# |
# |
# est une pointe de dimension 4.
# L’objectif est d’afficher des pointes d’une dimension donnée.
# Écrire un algorithme affichant p pointes (côte à côte) de dimension d.

# d=int(input("Veuillez entrer la dimension de/des flêche.s : "))
# p=int(input("Combien de pointes souhaitez-vous ? : "))
#
# for p in range(1,p+1):
#     print("_\t", end="")
# for d in range (1,d+1):
#     print()
#     for p in range(1,p+1):
#         print("|\t", end="")

# 10.Écrire un algorithme qui demande successivement 20 nombres à l’utilisateur, et qui lui dise ensuite  quel était le plus grand parmi ces 20 nombres.
nbMax=int
nbDemande=0
while nbDemande<2:
    nbDemande+=1
    nbUser=int(input(f"[{nbDemande}]Saisissez un nombre: "))
    if nbUser>nbMax:
        nbMax=nbUser
    else:
        pass

print(f"Le nombre le plus haut que vous ayez saisi est le {nbMax}")



