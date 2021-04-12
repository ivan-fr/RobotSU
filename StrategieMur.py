import math
from models import Robot
import datetime


class StrategieMur(object):
    def __init__(self, distance, stratAvancer, stratTourner):
        self.cote = 4
        self.coteParcouru = 0
        self.stratAvancer = stratAvancer
        self.stratTourner = stratTourner
        self.stratTourner.angle = 45

        self.distMur = 0.
        self.lastUpdate = None

    def start(self):
        self.distMur = 0.
        self.coteParcouru = 0
        self.lastUpdate = None
        self.robot.vitesse = 0.
        self.robot.lastCollision = False

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
            self.distMur = self.robot.getDistance()
            self.coteParcouru += 1

    def stop(self):
        # condition d'arret, lorsque que le robot a parcourut la distance souhaitee ou qu'il a rencontre un obstacle
        result = self.parcouruSimu >= self.distance or self.robot.lastCollision
        if result:
            self.robot.vitesse = 0.
        return result

    
