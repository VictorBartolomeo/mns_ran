#7. Écrivez l’algorithme qui affiche à l’écran les lignes suivantes :
# 10 11 12 13 14 15
# 20 21 22 23 24 25
# 30 31 32 33 34 35
# 40 41 42 43 44 45
# 50 51 52 53 54 55

i=0
for i in range (1,6):
    for n in range (1,6):
        print(f"{i}{n} ", end="")
    print("")