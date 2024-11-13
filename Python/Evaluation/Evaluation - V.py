#5. Vérifier si un mot est un palindrome

#Crée une fonction qui vérifie si un mot est un palindrome (un mot qui se lit de la même manière
#de gauche à droite et de droite à gauche).

def est_palindrome(mot):
    if len(mot) > 1:
        if mot == mot[::-1]:
            return f"le mot '{mot}' est un palindrome."
        else:
            return f"le mot '{mot}' n'est pas un palindrome."
    if len(mot) == 1:
        return f"la lettre '{mot}' est forcément un palindrome..."

print(est_palindrome("mom"))
print(est_palindrome("momo"))
print(est_palindrome("a"))
