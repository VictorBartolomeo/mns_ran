#6 Fonction de recherche

texte="C'est notre Raïs à nous : c'est monsieur René Coty. Un grand homme. Il marquera l'Histoire. Il aime les Cochinchinois, les Malgaches, les Marocains, les Sénégalais… c'est donc ton ami."
def contient_mot(texte, mot_cherche):
    if mot_cherche in texte:
        return True
    else:
        return False

print(contient_mot(texte, "Cochinchinois"))
print(contient_mot(texte, "Covfefe"))
