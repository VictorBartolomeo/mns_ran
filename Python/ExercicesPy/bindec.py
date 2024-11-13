nbDec=0
nbBin=str(input("entrez un binaire"))
exp=len(nbBin)-1
for i in nbBin:
    if i=="1":
        nbDec+=2**exp
        exp-=1
    else:
        exp-=1
print(nbDec)
        