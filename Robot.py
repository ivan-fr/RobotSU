import Vecteur
from math import sqrt, cos, sin, radians

class Robot(object):
    def __init__(self, x, y, vitesse, angle):
        self.vecteurDeplacement = None
        self._vitesse = 0.

        self.x = x
        self.y = y

        self.angle = angle
        self.vitesse = vitesse

    def avance(self,temps):
        """ int -> None 
        cette methode permet de faire avancer le robot selon un temps donné."""

        self.x += self.vecteurDeplacement.x * temps
        self.y += self.vecteurDeplacement.y * temps

    def rotation(self, angleRelative):
        """float -> void
        met à jour le vecteur deplacement du robot et son angle"""
        self.vecteurDeplacement = self.vecteurDeplacement.rotation(angleRelative)
        self.angle += angleRelative

    @property
    def vitesse(self):
        return self._vitesse

    @vitesse.setter
    def vitesse(self, vitesse):
        self.vecteurDeplacement = Vecteur.Vecteur(cos(radians(self.angle)) * vitesse, sin(radians(self.angle)) * vitesse)
        self._vitesse = vitesse
