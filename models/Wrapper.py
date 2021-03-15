from models import RobotIRL, Robot, Vecteur
import math

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

    @property
    def rotation(self):
        return self._rotation

    @rotation.setter
    def rotation(self, motor, angle):
        self.angle = angle
        if(motor == "MOTOR_LEFT"):
            self.RobotIRL.set_motor_dps(motor, angle)
            self.RobotIRL.set_motor_dps("MOTOR_RIGHT", -angle)
            self._degreParSeconde = angle
        elif(motor == "MOTOR_RIGHT"):
            self.RobotIRL.set_motor_dps(motor, angle)
            self.RobotIRL.set_motor_dps("MOTOR_LEFT", -angle)
            self._degreParSeconde = angle
        return

    @property
    def avance(self):
        return self.avance

    @avance.setter
    def avance(self, rayonRoue):
        """passer en parametres pour motor: MOTOR_LEFT ou MOTOR_RIGHT en fonction de vers où tourner
        ainsi que l'angle"""
        d = (self.vitesse * 360) / (2 * math.pi * rayonRoue)
        self.RobotIRL.set_motor_dps("MOTOR_LEFT+MOTOR_RIGHT", d)
        return

    def arretRobot(self):
        self.RobotIRL.set_motor_dps("MOTOR_LEFT+MOTOR_RIGHT", 0)
        return