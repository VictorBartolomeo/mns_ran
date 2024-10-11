#8.L’élève placé au fond de la classe, près du radiateur, est le meilleur de la classe.
# Pour tuer le temps,  il décide de plier une feuille en deux puis en deux, puis… en deux, puis…
# Écrivez un algorithme  qui calcule l’épaisseur du pliage final à partir du nombre de plis et de l’épaisseur initiale de la  feuille.

# import math (finalement non...)
epaisseurInitiale=int(input("Veuillez entrer l'épaisseur de la page en mm: "))
epaisseurFinale=epaisseurInitiale
nbPliages=int(input("Veuillez entrer le nombre de pliages effectué sur la feuille : "))

for nbPliages in range(1,nbPliages+1):
    epaisseurFinale+=epaisseurFinale

print(f"Avec une épaisseur de {epaisseurInitiale}mm et {nbPliages} pliages en deux, il en résulte une épaisseur de {epaisseurFinale}mm")