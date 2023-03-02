class Personnage:

    def __init__(self):
        self.y = 0
        self.x = 0
        print("Position initial du personnage : y =", self.y, "et x =", self.x)

    def haut(self):
        self.y+=1
        print("Le personnage monte")
    
    def bas(self):
        self.y-=1
        print("Le personnage descend")

    def gauche(self):
        self.x+=1
        print("Le personnage vas à gauche")

    def droite(self):
        self.x-=1
        print("Le personnage vas a droite")
        

    def position(self):
        print("Position du personnage : y =", self.y, "et x =", self.x)

personnage = Personnage()
personnage.haut()
personnage.position()
