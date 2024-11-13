#2. Vérification de nombre pair ou impair
def pair_ou_impair(nombre):
    if nombre % 2 == 0:
        return "pair"
    else:
        return "impair"
print("\nEx 2.")
print(pair_ou_impair(97))