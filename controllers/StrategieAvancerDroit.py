import math
from models import Robot
import datetime


class StrategieAvancerDroit(object):
    def __init__(self, distance, vitesse, terrainC, lastUpdate=None):
        self.distance = distance
        self.vitesse = vitesse
        self.tc = terrainC

        self.parcouru = 0
        self.lastUpdate = lastUpdate

    def start(self):
        self.parcouru = 0
        self.tc.robot.vitesse = self.vitesse

    def step(self):
        if self.lastUpdate is None:
            self.lastUpdate = datetime.datetime.now()
        else:
            now = datetime.datetime.now()
            deltaT = (now - self.lastUpdate).total_seconds()
            self.lastUpdate = now
            self.parcouru += self.vitesse * deltaT

    def stop(self):
        # condition d'arret, lorsque que le robot a parcourut la distance souhaitee ou qu'il a rencontre un obstacle
        result = self.parcouru >= self.distance or self.tc.robot.lastCollision
        if result:
            self.tc.robot.vitesse = 0
        return result
