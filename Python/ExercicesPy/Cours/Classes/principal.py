class Personnage:
    def __init__(self, nom, point_vie, intelligence,force,dexterite):
        self.nom = nom.capitalize()
        self.point_vie = point_vie
        self.intelligence = intelligence
        self.force = force
        self.dexterite = dexterite

    def info(self):
        print(f"Le personnage s'appelle {self.nom}")
    def __str__(self):
        print(f"Le personnage est fort de {self.force}")

guerrier=Personnage("Gromuskl",100,10,100,50)
magicien=Personnage("Gandalf",40,100,5,30)
voleur=Personnage("Balkany",60,70,20,100)
fouDuBus=Personnage("Stephane Brady",80,90,100,50)
paladin=Personnage("Paladin",90,90,100,50)

fouDuBus.__str__()