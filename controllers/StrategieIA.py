from models import Robot
from controllers import StrategieTournerIRL
import time

class StrategieIA(object):
    def __init__(self, wrapper, vitessemax):
        self.wrapper = wrapper
        self.vitessemax = vitessemax
        self.stopstrat = False
        self.stratTourner = StrategieTournerIRL.StrategieTournerIRL(wrapper, 20., 20.)
        
    def start(self):
        self.wrapper.robotIRL.stop()

    def step(self):
        while not self.stop():
            if self.wrapper.get_distance() < 250.:
                self.wrapper.vitesse = 0
                angleTourne = 0.
                while self.wrapper.get_distance() < 250.:
                    if angleTourne >= 360:
                        self.stopstrat = True
                        break
                    
                    self.stratTourner.start()
                    while not self.stratTourner.stop():
                        self.stratTourner.step()
                    angleTourne += 20
            else:
                self.wrapper.vitesse = self.vitessemax

    def stop(self):
        if self.stopstrat:
            self.wrapper.robotIRL.stop()
        return self.stopstrat
