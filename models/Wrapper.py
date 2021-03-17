from models import RobotIRL, Robot, Vecteur
import math
import time

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
    @vitesse.setter
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
        dist1 = self.RobotIRL.get_motor_position()
        time.sleep(1)
        dist2 = self.RobotIRL.get_motor_position()
        return (dist2 - dist1) == self.vitesse

    def arretRobot(self):
        self.RobotIRL.stop()
        dist1 = self.RobotIRL.get_distance()
        dist2 = self.RobotIRL.get_distance()
        return dist1 == dist2

    def get_distance(self):
        return self.RobotIRL.get_distance()

    def get_battery(self):
        battery = self.RobotIRL.get_voltage()
        if(battery < 10):
            print("Rechargez la batterie ", battery, "%")
        return battery