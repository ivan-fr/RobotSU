import math
from models import Robot,TerrainContinu
from controllers import StrategieTourner, StrategieAvancerDroit
import datetime

class StrategieMur(object):
    def __init__(self,Robot,Arene,StratAvancer,StratTourner):
        self.robot = Robot
        self.stratTourner = StrategieTourner.StrategieTourner(90,2,self.robot)
        self.Distance = self.robot.getDistance(Arene)
        self.stratAvancer = StrategieAvancerDroit.StrategieAvancerDroit(,vitesse,self.robot)
        
    def start():
        self.Distance = 0
        self.stratAvancer.start()
        self.stratTourner.start()
    
    def step():
        if self.stop():
            return
        elif sel
