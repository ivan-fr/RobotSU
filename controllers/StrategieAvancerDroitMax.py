from controllers import StrategieAvancerDroit, StrategieTourner
from models import Robot
import datetime
import math

class StrategieAvancerDroitMax(object):
    def __init__(self,Robot,vitesse,Distance,lastUpdate=None):
        self.robot = Robot
        self.vitessemax=vitesse
        self.vitesseinit = self.robot.vitesse
        self.Distance = Distance


        self.lastUpdate = lastUpdate
        
        
    def acceleration(self,deltaT):
        self.accel = (self.vitessemax - self.vitesseinit)/deltaT

    def deceleration(self):
        self.decel = math.pow(self.vitessemax,2)/(2*self.Distance)

    def start(self):
        self.parcouru = 0
        self.robot.vitesse = 0
        self.accel = 0
        self.decel = 0

    def step(self):
        if self.lastUpdate is None:
            self.lastUpdate = datetime.datetime.now()
        else:
            now = datetime.datetime.now()
            deltaT = (now - self.lastUpdate).total_seconds()
            self.lastUpdate = now
            if (not self.robot.collision(self, deltaT)) and (self.parcouru <=self.Distance) :
                self.acceleration(deltaT)
                self.robot.vitesse = self.vitessemax - self.accel * deltaT
            else : 
                self.deceleration()
                self.robot.vitesse = math.sqrt(self.decel * 2 * self.Distance)
    
    def stop(self):
        # condition d'arret, lorsque que le robot a parcourut la distance souhaitee ou qu'il a rencontre un obstacle
        result = self.parcouru >= self.Distance
        if result:
            self.robot.vitesse = 0
        return result
