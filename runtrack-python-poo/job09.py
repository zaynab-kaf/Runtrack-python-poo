class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.TVA = TVA / 100
        self.prixHT = prixHT


    def CalculerPrixTTC(self):
        return f"Voici le prix TTC des {self.nom} : {self.prixHT * (1 + self.TVA)}"

    def Aficher(self):
        return f"Voici le prix HT des {self.nom} : {self.prixHT}. La TVA est de : {self.TVA * 100}%, et le prix TTC est de : {self.prixHT * (1 + self.TVA)}"

    def modifnom(self, nom2):
        self.nom = nom2
        return self.nom

    def modifprix(self, prix2):
        self.prixHT = prix2
        return f"{self.prixHT} €"

produit1 = Produit("pommes rouges", 2, 20)
print(produit1.CalculerPrixTTC())
print(produit1.Aficher())
print(produit1.modifnom("pommes golden"))
print(produit1.modifprix(5))

produit2 = Produit("fraises", 6, 10)
print(produit2.CalculerPrixTTC())
print(produit2.Aficher())
print(produit2.modifnom("fraises bio"))
print(produit2.modifprix(15))

produit3 = Produit("mangues", 5, 20)
print(produit3.CalculerPrixTTC())
print(produit3.Aficher())
print(produit3.modifnom("mangues bio"))
print(produit3.modifprix(8))