import math
from models import Robot
from controllers import StrategieAvancerDroit
import datetime

class StrategieTriangleEquilateral(object):
    def __init__(self,Robot,Triangle,norme,lastUpdate=None):
        self.robot = Robot
        self.Triangle = Polygone.Triangle()
        self.lastUpdate = lastUpdate

    def start(self):
        self.parcouru = 0
        self.cote = 0

    def step(self):
        if self.stop():
            return

        self.robot.vitesse = self.vitesse
        for(i in range(3)):
             if self.lastUpdate is None:
            self.lastUpdate = datetime.datetime.now()
        else:
            now = datetime.datetime.now()
            deltaT = (now - self.lastUpdate).total_seconds()
            self.lastUpdate = now
            self.parcouru+=self.robot.vitesse * deltaT

            

    def stop(self):
        #condition d'arret lorsque le robot a parcouru les 4 cotes
        try:
            _ = self.liste_strategies[self.i_liste_strategies]
            return False
        except IndexError:
            return True

def 