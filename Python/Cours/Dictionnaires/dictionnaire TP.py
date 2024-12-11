stock = {
  "pomme" : 5 ,
  "banane" : 2 ,
  "chocolat" : 1 ,
  "cafe" : 4 
}

def afficher_stock(stock):
  for produit, quantite in stock.items():
    print(f"{produit} : {quantite}")

def mettre_a_jour_stock(stock):
    produit = input("quel produit voulez vous mettre a jour ? ")
    quantite = int(input("quel est la nouvelle quantite ? "))
    stock[produit] = quantite

def gestion(stock):
    while True:
        choix = input("Afficher le stock : (1) , \nMettre a jour un produit (2) , \nQ pour quitter\nVotre choix : ")
        if choix == "1":
            afficher_stock(stock)
        elif choix == "2":
            mettre_a_jour_stock(stock)
        elif choix == "q":
            break
        else:
            print("choix invalide")


gestion(stock)
print("fin du programme")
afficher_stock(stock)
