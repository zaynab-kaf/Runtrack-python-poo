class Animal:
    global age
    age = 0
    print("L'âge de l'animal est de", age, "an")

    def vieillir():
        global age
        age+=1
        print("L'âge de l'animal est de", age, "an")

    def nommer():
        prénom = input("Comment voulez-vous nommer votre animal ?")
        print("Votre animal se nomme",prénom)
    
Animal() #ÂGE INITIAL DE L'ANIMAL     
Animal.vieillir() #ÂGE DE L'ANIMAL APRES LAVOIR FAIT VIEILLIR
Animal.nommer() # NOMMER L'ANIMAL
