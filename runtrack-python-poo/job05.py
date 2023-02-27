class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Le point a pour abscissse : {self.x} et pour ordonnée : {self.y}")

    def afficherX(self):
        print(f"Le point a pour abscissse : {self.x}")

    def afficherY(self):
        print(f"Le point a pour ordonnée : {self.y}")

    def changerX(self, nouveauX):
        ancienX = self.x
        self.x = nouveauX

        print(f"Le point avait pour abscissse : {ancienX}, maintenant son abscisse est : {self.x}")

    def changerY(self, nouveauY):
        ancienY = self.y
        self.y = nouveauY

        print(f"Le point avait pour ordonnée : {ancienY}, maintenant son ordonnée est : {self.y}")

point = Point(0, 0)
point.afficherLesPoints()
point.changerX(100)
point.changerY(30)
