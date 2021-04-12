from models import Robot
from controllers import StrategieAvancerDroit, StrategieTourner

class StrategieTourArene(object):
    def __init__(self, stratTourner, stratAvancer, Robot, TerrainContinu):
        self.Robot = Robot
        self.stratTourner = stratTourner
        self.stratAvancer = stratAvancer
        self.tc = TerrainContinu

    def start(self):
        self.nbcotes = 0
        self.Robot.vitesse = 0
        self.stratTourner.start()

    def step(self):
        if self.stop():
            return
        if self.Robot.getDistance(tc) < 0.05:
            while not self.stratTourner.stop():
                self.stratTourner.step()
            self.stratTourner.start()
            self.nbcotes += 1
        else:
            self.stratAvancer.step()
            self.stratAvancer.start()
        
    def stop():
        return self.nbcotes >= 4
