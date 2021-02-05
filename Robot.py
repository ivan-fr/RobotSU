from Terrain import *
import math
import Vecteur

class Robot(object):
    def __init__(self, x, y, vitesse, angle):
        self.x = x
        self.y = y
        self._vitesse = vitesse
        self.angle = angle
        self.vecteurDeplacement = Vecteur(cos(angle) * vitesse, sin(angle) * vitesse)


    def avance(self,temps):
        """ int -> None 
        cette methode permet de faire avancer le robot selon un temps donné."""

        self.x=self.x+(self.vitesse*temps)
        self.y=self.y+(self.vitesse*temps)

    def rotation(self, angle):
        """int -> Vecteur
        retourne le vecteur apres une rotation de l'angle"""
        vv = Vecteur.__mul__(self.vitesse)
        vx = vv.x * math.cos(angle) - vv.y * math.sin(angle)
        vy = vv.x * math.sin(angle) + vv.y * math.cos(angle)
        return Vecteur.Vecteur(vx, vy)

    @vitesse.setter
    def vitesse(self, vitesse):
        self.vecteurDeplacement = Vecteur(cos(self.angle) * vitesse, sin(self.angle) * vitesse)
        self._vitesse = vitesse

    @property
    def vitesse(self):
        return self._vitesse