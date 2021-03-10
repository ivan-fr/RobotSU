from models import Robot
import datetime

class StrategieTourner(object) :

    def __init__(self, angleTarget, degreParSeconde, robot):
        self.robot = robot
        self.angleTarget = angleTarget
        self.angleApplique = 0.
        self.degreParSeconde = degreParSeconde
        self.lastUpdate = None

    def start(self):
        self.angleApplique = 0.
        self.lastUpdate = None
        self.robot._degreParSeconde = 0.

    def step(self):
        self.robot._degreParSeconde = self.degreParSeconde
        if self.lastUpdate is None:
            self.lastUpdate = datetime.datetime.now()
        else:
            now = datetime.datetime.now()
            deltaT = (now - self.lastUpdate).total_seconds()
            self.lastUpdate = now
            self.angleApplique += deltaT * self.robot._degreParSeconde

    def stop(self):
        # condition d'arret, si le robot a bien tourne
        result = self.angleApplique >= self.angleTarget
        if result:
            self.robot._degreParSeconde = 0.

        return result
