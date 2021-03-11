from models import RobotIRL, Robot, Vecteur
import math

class Wrapper(object):
    def __init__(self, RobotIRL):
        self.RobotIRL = RobotIRL
        self._vitesse = 0
        self._degreParSeconde = 0
        self._vecteurDeplacement = None
        self.bouger = 0

    @property
    def vecteurDeplacement(self):
        return self._vecteurDeplacement

    @vecteurDeplacement.setter
    def vecteurDeplacement(self, vecteurDeplacement):
        self._vecteurDeplacement = vecteurDeplacement
        self._degreParSeconde = self.fromVecteurToAngle(vecteurDeplacement)
        self.bouger = self.mouvement()

    def fromVecteurToAngle(self, vecteurDeplacement):
        x = vecteurDeplacement.x
        y = vecteurDeplacement.y
        return 2*math.atan(y/(x+math.sqrt(x**2 + y**2)))

    @property
    def degreParSeconde(self):
        return self.degreParSeconde

    def mouvement(self):
        """passer en parametres pour motor: MOTOR_LEFT ou MOTOR_RIGHT en fonction de vers où tourner
        ainsi que l'angle"""
            self.RobotIRL.set_motor_dps("MOTOR_RIGHT", self.degreParSeconde)
        