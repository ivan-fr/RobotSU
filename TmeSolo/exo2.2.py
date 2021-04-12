import math
from models import Robot
from controllers import StrategieTourner, StrategieAvancerDroit
import datetime

class StrategieTriangleEquilateral(object):
    def __init__(self,Robot,Polygone,distance,vitesse,stratTourner,startAvancer):
        self.robot = Robot
        self.lastUpdate = lastUpdate
        self.stratTourner = StrategieTourner.StrategieTourner(((self.cote - 2)*math.pi)/2 ,2,self.robot)
        self.stratAvancer = StrategieAvancerDroit.StrategieAvancerDroit(distance,vitesse,self.robot)
        self.cote = len(Polygone.liste_vecteur)

    def start():
        self.stratTourner.start()
        self.stratAvancer.start()

    def step():
        for i in range(self.cote):
            StratAvancer.step()
            StratTourner.step()

    
        


