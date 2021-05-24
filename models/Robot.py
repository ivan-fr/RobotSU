from models import Vecteur
from math import cos, sin, radians
import datetime


class Robot(object):
    def __init__(self, x, y, vitesse=0., angle=0., vecteurDeplacement=None, lastCollision=False):
        self.vecteurDeplacement = None
        self._vitesse = 0.
        self._degreParSeconde = 0.
        self._lastUpdate = None

        self.x = x
        self.y = y

        self.angle = angle % 360.

        if self.angle > 180.:
            self.angle -= 360.

        self.vitesse = vitesse

        self.lastCollision = lastCollision

    def __str__(self):
        """ -> str
        Permet de retourner une chaine de caractère représentant l'objet robot
        """
        return "Robot(cood.(" + str(self.x) + "," + str(self.y) + "),vitesse:" + str(
            self.vitesse) + "mm/s, angle:" + str(self.angle) + "°)"

    def avance(self, deltaTemps):
        """ int -> None 
        cette methode permet de faire avancer le robot selon un temps donné."""
        self.x += self.vecteurDeplacement.x * deltaTemps
        self.y += self.vecteurDeplacement.y * deltaTemps

    def collision(self, terrainContinu, temps):
        return terrainContinu.collision((self.x, self.y), self.vecteurDeplacement * temps)

    def rotation(self, deltaTemps):
        """float -> void
        met à jour le vecteur deplacement du robot et son angle"""
        angleRelative = self._degreParSeconde * deltaTemps
        self.vecteurDeplacement = self.vecteurDeplacement.rotation(angleRelative)
        self.angle += angleRelative
        self.angle %= 360

        if self.angle > 180.:
            self.angle -= 360.

    def update(self, tc):
        if self._lastUpdate is None:
            self._lastUpdate = datetime.datetime.now()
        else:
            now = datetime.datetime.now()
            deltaT = (now - self._lastUpdate).total_seconds()
            self._lastUpdate = now
            self.rotation(deltaT)

            if not self.collision(tc, deltaT):
                self.avance(deltaT)
            else:
                self.lastCollision = True

    def getDistance(self, tc):
        vUnitaire = Vecteur.Vecteur(cos(radians(self.angle)) * 1,
                                    sin(radians(self.angle)) * 1)
        while not tc.collision((self.x, self.y), vUnitaire):
            vUnitaire += vUnitaire

        return vUnitaire.norme()

    @property
    def vitesse(self):
        return self._vitesse

    @vitesse.setter
    def vitesse(self, vitesse):
        self.vecteurDeplacement = Vecteur.Vecteur(cos(radians(self.angle)) * vitesse,
                                                  sin(radians(self.angle)) * vitesse)
        self._vitesse = vitesse
