from models import RobotIRL, Robot, Vecteur
import math
rayonRoue = 10
class Wrapper(object):
    def __init__(self, RobotIRL):
        self.RobotIRL = RobotIRL
        self._vitesse = 0
        self._rotation = 0
        self._avance = 0
        self.angle = 1

    @property
    def vitesse(self):
        return self._vitesse
    @vitesses.setter
    def vitesse(self, vitesse):
        self._vitesse = vitesse
    @property
    def rotation(self):
        return self._rotation

    @rotation.setter
    def rotation(self, angle):
        self.angle = angle
        self.RobotIRL.set_motor_dps("MOTOR_RIGHT", angle)
        self.RobotIRL.set_motor_dps("MOTOR_LEFT", -angle)
        return

    @property
    def avance(self):
        return self.avance

    @avance.setter
    def avance(self):
        """passer en parametres pour motor: MOTOR_LEFT ou MOTOR_RIGHT en fonction de vers où tourner
        ainsi que l'angle"""
        global rayonRoue
        dps = (self.vitesse * 360) / (2 * math.pi * rayonRoue)
        self.RobotIRL.set_motor_dps("MOTOR_LEFT+MOTOR_RIGHT", dps)
        return

    def arretRobot(self):
        self.RobotIRL.set_motor_dps("MOTOR_LEFT+MOTOR_RIGHT", 0)
        return