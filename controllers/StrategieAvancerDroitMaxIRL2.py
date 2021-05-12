import math
from models import Robot
import datetime


class StrategieAvancerDroitMaxIRL2(object):
    def __init__(self, wrapper, vitesse):
        self.vitesse = vitesse
        self.wrapper = wrapper
        self.distance = wrapper.get_distance()

        self.parcouruIRL = 0.

    def start(self):
        self.parcouruIRL = 0
        self.wrapper.vitesse = 0.

    def step(self):
        if self.stop():
            return
        self.wrapper.vitesse = self.vitesse

        if self.wrapper.vitesse < 1500. :
            self.vitesse += self.vitesse * 1.5
            self.wrapper.vitesse = self.vitesse
        else :
            self.wrapper.vitesse = 1500.

        self.parcouruIRL += self.wrapper.last_avancement

    def stop(self):
        #inferieur a 20 ?
        result = (self.parcouruIRL >= self.distance or self.wrapper.robotIRL.get_distance() * 1e-1 < 30 )
        if result:
            self.wrapper.vitesse = 0.
        return result
