from importlib.metadata import pass_none

from select import select


class Produit:
    def __init__(self, nom, prix_HT,TVA,qty_stock):
        self.nom = nom
        self.prix_HT = prix_HT
        self.TVA = TVA
        self.qty_stock = qty_stock

    def prixTTC(self):
        return (self.prix_HT*(self.TVA/100))+self.prix_HT


class Magasin:
    def __init__(self, liste_produit,):
        self.liste_produit = liste_produit

    def ruptureStock(self):
        nbHorsStock=0
        for produit in self.liste_produit:
            if produit.qty_stock<=0:
                print(f"{produit.nom} est hors stock.")
                nbHorsStock+=1
            else:
                pass
        print(f"Total : {nbHorsStock} produits hors stock / {len(self.liste_produit)} produits au total.")

    def CA(self):
        total=0
        for produit in fnac.liste_produit:
            total+=(produit.prixTTC()*produit.qty_stock)
        return total

    def ajoutProduit(self):
        liste_produit.append(Produit(
            str(input("Entrez le nom du produit : ")),
                              float(input("Entrez le prix HT du produit : ")),
                              float(input("Entrez le TVA du produit : ")),
                              int(input("Entrez le quantité en stock du produit : "))))

    def modifQty(self):
        nomModif=str(input("Entrez le nom du produit à modifier: "))
        for produit in self.liste_produit:
            if produit.nom == nomModif:
                modifQty=int(input(f"Entrez la correction de quantité du produit {nomModif} : "))
                produit.qty_stock=modifQty
                print(f"La quantité du produit {nomModif} est désormais : {produit.qty_stock}")


bateau=Produit("Boat",12000,20,1)
chimpanze=Produit("Sinj",1800,20,12)
pates=Produit("pates",2.50,5.5,0)

liste_produit=[bateau,chimpanze,pates]
fnac=Magasin(liste_produit)

print(Produit(chimpanze.nom,chimpanze.prix_HT,chimpanze.TVA,chimpanze.qty_stock))

print ("MENU:")
print("1. Saisir un nouveau produit")
print("2. Modifier la quantité d'un produit")
print("3. Lister les produits en rupture de stock")
print("4. Lister le CA réalisable à ce jour")

choixMenu=int(input("\n\tVeuillez choisir une option: "))

if choixMenu==1:
    fnac.ajoutProduit()
if choixMenu==2:
    fnac.modifQty()
if choixMenu==3:
    fnac.ruptureStock()
if choixMenu==4:
    print(f"{fnac.CA()}€ de moulah.")



# print(Produit.prixTTC(bateau))

# print(fnac.CA())
# fnac.ruptureStock()
# fnac.ajoutProduit()





