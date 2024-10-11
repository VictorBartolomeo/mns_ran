# 10.Écrire un algorithme qui demande successivement 20 nombres à l’utilisateur, et qui lui dise ensuite  quel était le plus grand parmi ces 20 nombres.


nbDemande=1
nbUser=int(input(f"[{nbDemande}]Saisissez un nombre: "))
nbMax=nbUser
while nbDemande<20:
    nbDemande+=1
    nbUser=int(input(f"[{nbDemande}]Saisissez un nombre: "))
    if nbUser>nbMax:
        nbMax=nbUser
    else:
        pass

print(f"Le nombre le plus haut que vous ayez saisi est le {nbMax}")