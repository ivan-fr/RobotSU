from models import Robot
from controllers import StrategieTournerIRL
import time

class StrategieIA(object):
    def __init__(self, Robot, vitessemax):
        self.robot = Robot
        self.vitessemax = vitessemax
        self.stopstrat = False
        self.stratTourner = StrategieTourner.StrategieTourner(Robot, 20., 20.)
        
    def start(self):
        self.robot.vitesse = 0

    def step(self):
        while not self.stop():
            if self.robot.get_distance() < 250.:
                self.robot.vitesse = 0
                angleTourne = 0.
                while self.robot.get_distance() < 250.:
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