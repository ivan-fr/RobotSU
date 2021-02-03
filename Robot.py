from Terrain import *
class Robot(object):
    def __init__(self, x, y, vitesse, angle):
        self.x = x
        self.y = y
        self.vitesse = vitesse
        self.angle = angle


    def avance(self,temps):
        """ int -> None 
        cette methode permet de faire avancer le robot selon un temps donné."""

        self.x=self.x+(self.vitesse*temps)
        self.y=self.y+(self.vitesse*temps)

