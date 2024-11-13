#3.Inverser une chaîne de caractères
texte="le chien est sur la balançoire, mais que fait-il là ?"
def inverser_chaine(texte):
    #::-1 retourne les éléments en démarrant de la fin (index -1= dernier élément)
    return texte[::-1]
print("\nEx 3.")
print(inverser_chaine(texte))