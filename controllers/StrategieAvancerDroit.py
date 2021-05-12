import math
from models import Robot
import datetime


class StrategieAvancerDroit(object):
    def __init__(self, robot, distance, vitesse):
        self.distance = distance
        self.vitesse = vitesse
        self.robot = robot

        self.parcouruSimu = 0.
        self.lastUpdate = None

    def start(self):
        self.parcouruSimu = 0.
        self.lastUpdate = None
        self.robot.vitesse = 0.
        self.robot.lastCollision = False

    def step(self):
        if self.stop():
            return
            
        self.robot.vitesse = self.vitesse

        if self.lastUpdate is None:
            self.lastUpdate = datetime.datetime.now()
        else:
            now = datetime.datetime.now()
            deltaT = (now - self.lastUpdate).total_seconds()
            self.lastUpdate = now
            self.parcouruSimu += self.vitesse * deltaT

    def stop(self):
        # condition d'arret, lorsque que le robot a parcourut la distance souhaitee ou qu'il a rencontre un obstacle
        result = self.parcouruSimu >= self.distance or self.robot.lastCollision
        if result:
            self.robot.vitesse = 0.
        return result
