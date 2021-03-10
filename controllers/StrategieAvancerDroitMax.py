from controllers import StrategieAvancerDroit, StrategieTourner
from models import Robot
import datetime

class StrategieAvancerDroitMax(object):
    def __init__(self,Robot,vitesse,lastUpdate=None):
        self.robot = Robot
        self.vitessemax=vitesse
        self.vitesseinit = self.robot.vitesse


        self.lastUpdate = lastUpdate
        
        
    def acceleration(self,deltaT):
        self.accel = (self.vitessemax - self.vitesseinit)/deltaT

    def start(self):
        self.parcouru = 0
        self.robot.vitesse = 0
        self.accel = 0

    def step(self):
        if self.lastUpdate is None:
            self.lastUpdate = datetime.datetime.now()
        else:
            now = datetime.datetime.now()
            deltaT = (now - self.lastUpdate).total_seconds()
            self.lastUpdate = now
            if not self.robot.collision(self, deltaT):
                self.acceleration(deltaT)
                self.robot.vitesse = self.vitessemax - self.accel * deltaT
    
