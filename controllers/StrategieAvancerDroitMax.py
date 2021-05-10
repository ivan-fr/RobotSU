from controllers import StrategieAvancerDroit, StrategieTourner
from models import Robot
import datetime
import math

class StrategieAvancerDroitMax(object):
    def __init__(self,Robot,vitesse,TerrainContinu,lastUpdate=None):
        self.robot = Robot
        self.vitesse=vitesse
        self.Distance = self.robot.getDistance(TerrainContinu)
        self.parcouru = 0

        self.lastUpdate = lastUpdate
        

    def start(self):
        self.parcouru = 0
        self.lastUpdate=None
        self.robot.vitesse = 0

    def step(self):
        if self.stop():
            return
            
        self.robot.vitesse = self.vitesse
        
        if self.lastUpdate is None:
            self.lastUpdate = datetime.datetime.now()
        else:
            now = datetime.datetime.now()
            deltaT = (now - self.lastUpdate).total_seconds()
            self.lastUpdate = now
            self.parcouru+= self.vitesse * deltaT
    
    def stop(self):
        # condition d'arret, lorsque que le robot a parcourut la distance souhaitee ou qu'il a rencontre un obstacle
        result = (self.parcouru >= self.Distance)
        if result:
            self.robot.vitesse = 0
        return result