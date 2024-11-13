# Ex1

# prenoms =["Alice", "Bob", "Charlie", "David","Eve"]

# print(prenoms[0])
# longueur=len(prenoms)
# print(prenoms[longueur-1])
# prenoms.append("Frank")
# remplacement=prenoms.index("David")
# prenoms[remplacement]= "Daniel"
# prenoms.remove("Charlie")
# print(len(prenoms))

# print(prenoms)

#Ex 2

# nb=[10,20,30,40,50]
# index=0
# somme=0
# for i in nb:
#     somme=nb[index]+somme
#     index+=1

# print(somme)

# moyenne=0
# moyenne=somme/len(nb)
# print(moyenne)

# nbMax=nb[0]
# nbMin=nb[0]
# index=0
# for i in nb:
#     if nb[index]>nbMax:
#         nbMax=nb[index]
#     elif nb[index]<nbMin:
#         nbMin=nb[index]
#     else:
#         pass
#     index+=1
# print(nbMax)
# print(nbMin)

# Ex 3

# liste=[8,24,34,3,6]
# print(liste)
# reverseListe=[]
# for i in range(len(liste)):
#     nvNb= liste[(len(liste)-1)-i]
#     reverseListe.append(nvNb)
# print(reverseListe)

#Ex 5

# liste =[1, 3, 7, 8, 7, 5, 6, 7, 9, 2]
# print(liste.count(int(input("Quel nombre voulez vous tester ? : "))))

#Ex 6

# liste=[1,4,5,8,9,82,1,68,4,5,61,3856,461,34,5,3,2,46,6,4,2,5,3,19,7,97,5,1,3,5]
# liste_pairs=[]
# liste_impairs=[]
# for i in liste:
#     if i%2==0:
#         liste_pairs.append(i)
#     else:
#         liste_impairs.append(i)
# print(f"Pairs : {liste_pairs}")
# print(f"Impairs : {liste_impairs}")

#Ex 7

# liste=[1,4,5,8,9,82,1,68,4,5,61,3856,461,34,5,3,2,46,6,4,2,5,3,19,7,97,5,1,3,5]
# pairs=0
# impairs=0
# for i in liste:
#     if i%2==0:
#         pairs+=1
#     else:
#         impairs+=1
# print(f"Il y a {pairs} pairs et {impairs} impairs.")


