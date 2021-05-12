from models import Robot
from controllers import StrategieTourner
import time

class StrategieIASimulé(object):
    def __init__(self, Robot, vitessemax,TerrainContinu):
        self.robot = Robot
        self.tc = TerrainContinu
        self.vitessemax = vitessemax
        self.stopstrat = False
        self.stratTourner = StrategieTourner.StrategieTourner(Robot, 20., 20.)
        
    def start(self):
        self.robot.vitesse = 0
       
    def step(self):
        if self.robot.get_distance(tc) < 5.:
            self.robot.vitesse = 0
            angleTourne = 0.
            while self.robot.get_distance(tc) < 5.:
                if angleTourne >= 360:
                    self.stopstrat = True
                    break
                    
                self.stratTourner.start()
                while not self.stratTourner.stop():
                    self.stratTourner.step()
                angleTourne += 20
        else:
            self.robot.vitesse = self.vitessemax

    def stop(self):
        if self.stopstrat:
            self.robot.vitesse = 0
        return self.stopstrat