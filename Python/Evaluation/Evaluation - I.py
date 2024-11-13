#1. SOmme de 1 à n

def somme_n_entiers(n):
    somme = 0
    for i in range(1, n+1):
        somme += i
    return somme

print("Ex 1.")
print(somme_n_entiers(10))