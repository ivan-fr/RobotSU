from controllers import StrategieAvancerDroit, StrategieTourner
from models import Robot
import datetime
import math

class StrategieAvancerDroitMax(object):
    def __init__(self,Robot,vitesse,Distance,lastUpdate=None):
        self.robot = Robot
        self.vitessemax=vitesse
        self.Distance = Distance
        self.parcouru = 0

        self.lastUpdate = lastUpdate
        
        
    def acceleration(self,deltaT):
        self.accel = (self.vitessemax - self.robot.vitesse)/deltaT

    def start(self):
        self.parcouru = 0
        self.lastUpdate=None
        self.accel = 0
        self.robot.vitesse = 0

    def step(self):
        self.robot.vitesse = 1
        if self.stop():
            return 
        if self.lastUpdate is None:
            self.lastUpdate = datetime.datetime.now()
        else:
            now = datetime.datetime.now()
            deltaT = (now - self.lastUpdate).total_seconds()
            self.lastUpdate = now
            self.acceleration(deltaT)
            self.robot.vitesse = self.vitessemax - self.accel * deltaT
            self.parcouru+=self.robot.vitesse * deltaT

    
    def stop(self):
        # condition d'arret, lorsque que le robot a parcourut la distance souhaitee ou qu'il a rencontre un obstacle
        result = (self.parcouru >= self.Distance)
        if result:
            self.robot.vitesse = 0
        return result
