import math
from models import Robot
from controllers import StrategieTourner
import datetime

class StrategieTriangleEquilateral(object):
    def __init__(self,Robot,lastUpdate=None,stratTourner):
        self.robot = Robot
        self.Triangle = Polygone.Triangle()
        self.lastUpdate = lastUpdate
        self.stratTourner = StrategieTourner.StrategieTourner(60 , 2,self.robot)
   
    def start(self):
        self.parcouru = 0
        self.robot.lastCollision = False
        self.stratTourner.start()

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
            

            self.robot._degreParSeconde = self.degreParSeconde

            if self.lastUpdate is None:
                self.lastUpdate = datetime.datetime.now()
            else:
                now = datetime.datetime.now()
                deltaT = (now - self.lastUpdate).total_seconds()
                self.lastUpdate = now
                self.angleApplique += deltaT * self.robot._degreParSeconde 




