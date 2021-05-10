import math
from models import Robot
import datetime


class StrategieAvancerDroitMaxIRL2(object):
    def __init__(self, wrapper, vitesse,lastUpdate=None):
        self.vitesse = vitesse
        self.wrapper = wrapper
        self.vitesse = wrapper.vitesse
        self.distance = wrapper.get_distance()

        self.parcouruIRL = 0.
        self.lastUpdate = lastUpdate

    def start(self):
        self.parcouruIRL = 0
        self.lastUpdate=None
        self.wrapper.vitesse = 0.

    def step(self):
        if self.stop():
            return
            
        self.wrapper.vitesse = self.vitesse

        self.parcouruIRL += self.wrapper.last_avancement

    def stop(self):
        #inferieur a 20 ?
        result = (self.parcouruIRL >= self.distance or self.wrapper.robotIRL.get_distance() * 1e-1 < 3)
        if result:
            self.wrapper.vitesse = 0.
            self.wrapper.robotIRL.stop()
        return result
