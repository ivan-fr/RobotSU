import math
from models import Robot
from models import Wrapper
import datetime


class StrategieAvancerDroit(object):
    def __init__(self, distance, vitesse, robot, wrapper):
        self.distance = distance
        self.vitesse = vitesse
        self.robot = robot
        self.wrapper = wrapper

        self.parcouruSimu = 0.
        self.parcouruIRL = 0.
        self.lastUpdate = None

    def start(self):
        self.parcouruSimu = 0.
        self.parcouruIRL = 0.
        self.lastUpdate = None
        self.robot.vitesse = 0.

    def step(self):
        if self.stop():
            return
            
        self.robot.vitesse = self.vitesse
        self.wrapper.vitesse = self.robot.vitesse

        if self.lastUpdate is None:
            self.lastUpdate = datetime.datetime.now()
        else:
            now = datetime.datetime.now()
            deltaT = (now - self.lastUpdate).total_seconds()
            self.lastUpdate = now
            self.parcouruSimu += self.vitesse * deltaT
            self.parcouruIRL += self.wrapper.last_avancement

    def stop(self):
        # condition d'arret, lorsque que le robot a parcourut la distance souhaitee ou qu'il a rencontre un obstacle
        result = self.parcouruSimu >= self.distance or self.parcouruIRL >= self.distance
        if result:
            self.robot.vitesse = 0.
            self.wrapper.RobotIRL.stop()
        return result
