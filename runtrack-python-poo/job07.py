class Personnage():
    global y, x
    y = 0
    x = 0
    print("Position initial du personnage : y =", y, "et x =", x)

    def haut():
        global y,x
        y+=1
        print("Le personnage monte")
    
    def bas():
        global y,x
        y-=1
        print("Le personnage descend")

    def gauche():
        global y,x
        x+=1
        print("Le personnage vas à gauche")

    def droite():
        global y,x
        x-=1
        print("Le personnage vas a droite")
        

    def position():
        print("Position du personnage : y =", y, "et x =", x)


Personnage()
Personnage.haut()
Personnage.position()
