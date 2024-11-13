#9. Classe CompteBancaire avec dépôt et retrait

class CompteBancaire:
    def __init__(self, solde):
        self.solde = solde


    def deposer(self, montant):
        self.solde += montant
        print(f"Hop! On vient de créditer {montant} Francs CFA sur votre compte. Vous possédez désormais {self.solde} Francs CFA.")

    def retirer(self, montant):
        if montant > self.solde: #on teste si on a le solde necessaire au retrait
            print(f"Désolé. Votre solde ({self.solde}) est inférieur au montant ({montant}) du retrait. Veuillez être plus riche pour procéder.")
        else:
            if montant == self.solde: #On alerte le client si il n'a plus d'argent
                print(f"Attention ! VOus venez de retirer {montant} Francs CFA de votre compte. Votre compte est à {self.solde} Francs CFA. Petit pauvre va.")
            else:
                self.solde -= montant
                print(f"Hop! VOus venez de retirer {montant} Francs CFA de votre compte. Vous possédez désormais {self.solde} Francs CFA.")


hubert_credit_mut=CompteBancaire(117)

hubert_credit_mut.deposer(100)
hubert_credit_mut.retirer(317)
hubert_credit_mut.retirer(100)