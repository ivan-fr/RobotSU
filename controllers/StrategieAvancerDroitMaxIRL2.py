import math
from models import Robot
import datetime


class StrategieAvancerDroitMaxIRL2(object):
    def __init__(self, wrapper, vitessemax,lastUpdate=None):
        self.vitessemax = vitessemax
        self.wrapper = wrapper
        self.vitesseinit = wrapper.vitesse
        self.distance = wrapper.get_distance()

        self.parcouruIRL = 0.
        self.lastUpdate = lastUpdate

    # reecrire fonction acceleration IRL ?
    def acceleration(self,deltaT):
        self.accel = (self.vitessemax - self.vitesseinit)/deltaT

    def start(self):
        self.parcouruIRL = 0
        self.lastUpdate=None
        self.accel = 0
        self.wrapper.vitesse = 0.

    def step(self):
        if self.stop():
            return
        
        if self.lastUpdate is None:
            self.lastUpdate = datetime.datetime.now()
        else:
            now = datetime.datetime.now()
            deltaT = (now - self.lastUpdate).total_seconds()
            self.lastUpdate = now
            self.acceleration(deltaT)
            self.wrapper.vitesse = self.wrapper.vitesse + ((self.accel * deltaT)/2)
            self.parcouruIRL += self.wrapper.last_avancement

    def stop(self):
        #inferieur a 20 ?
        result = self.parcouruIRL >= self.distance or self.wrapper.RobotIRL.get_distance() * 1e-1 < 3
        if result:
            self.wrapper.vitesse = 0.
        return result
