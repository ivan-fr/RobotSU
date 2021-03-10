from controllers import StrategieAvancerDroit, StrategieTourner
from models import Robot
import datetime

class StrategieAvancerDroitMax(object):
    def __init__(self,terrainC,vitesse,lastUpdate=None):
        self.tc = terrainC
        self.vitessemax=vitesse
        self.vitesseinit = self.tc.robot.vitesse


        self.lastUpdate = lastUpdate
        
        
    def acceleration(self,deltaT):
        self.accel = (self.vitessemax - self.vitesseinit)/deltaT

    def start(self):
        self.parcouru = 0
        self.tc.robot.vitesse = 0

    def step(self):
        if self.lastUpdate is None:
            self.lastUpdate = datetime.datetime.now()
        else:
            now = datetime.datetime.now()
            deltaT = (now - self.lastUpdate).total_seconds()
            self.lastUpdate = now
            if not self.tc.robot.collision(self, deltaT):
                self.acceleration(deltaT)
                self.tc.robot.vitesse = self.vitessemax - self.accel * deltaT
    
