import math
from models import Robot
import datetime


class StrategieAvancerDroitIRL(object):
    def __init__(self, wrapper, distance, vitesse):
        self.distance = distance
        self.vitesse = vitesse
        self.wrapper = wrapper

        self.parcouruIRL = 0.

    def start(self):
        self.parcouruIRL = 0.
        self.wrapper.vitesse = 0.

    def step(self):
        if self.stop():
            return
            
        if self.wrapper.vitesse < 10e-3:
            self.wrapper.vitesse = self.vitesse

        self.parcouruIRL += self.wrapper.last_avancement

    def stop(self):
        # condition d'arret, lorsque que le robot a parcourut la distance souhaitee ou qu'il a rencontre un obstacle
        result = self.parcouruIRL >= self.distance or self.wrapper.robotIRL.get_distance() < 50
        if result:            
            self.wrapper.vitesse = 0.
        return result
