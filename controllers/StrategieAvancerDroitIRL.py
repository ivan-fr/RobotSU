import math
from models import Robot
import datetime


class StrategieAvancerDroitIRL(object):
    def __init__(self, wrapper, distance, vitesse):
        self.distance = distance
        self.vitesse = vitesse
        self.wrapper = wrapper

        self.parcouruIRL = 0.
        self.lastUpdate = None

    def start(self):
        self.parcouruIRL = 0.
        self.lastUpdate = None
        self.wrapper.RobotIRL.stop()

    def step(self):
        if self.stop():
            return
            
        self.wrapper.vitesse = self.vitesse

        if self.lastUpdate is None:
            self.lastUpdate = datetime.datetime.now()
        else:
            now = datetime.datetime.now()
            deltaT = (now - self.lastUpdate).total_seconds()
            self.lastUpdate = now
            self.parcouruIRL += self.wrapper.last_avancement

    def stop(self):
        # condition d'arret, lorsque que le robot a parcourut la distance souhaitee ou qu'il a rencontre un obstacle
        result = self.parcouruIRL >= self.distance or self.wrapper.RobotIRL.get_distance() < 2
        if result:
            self.wrapper.RobotIRL.stop()
        return result
