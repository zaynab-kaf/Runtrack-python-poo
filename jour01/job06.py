class Animal:
    def __init__(self):
        self.age = 0
        print("L'âge de l'animal est de", self.age, "an")

    def vieillir(self):
        self.age+=1
        print("L'âge de l'animal est de",self.age, "an")

    def nommer(self):
        self.prénom = input("Comment voulez-vous nommer votre animal ?")
        print("Votre animal se nomme",self.prénom)
    
animal = Animal() #ÂGE INITIAL DE L'ANIMAL    
animal.vieillir() #ÂGE DE L'ANIMAL APRES LAVOIR FAIT VIEILLIR
animal.nommer() # NOMMER L'ANIMAL
