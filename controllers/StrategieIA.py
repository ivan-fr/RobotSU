from models import Robot
from controllers import StrategieTournerIRL
import time

class StrategieIA(object):
    def __init__(self, wrapper, vitessemax):
        self.wrapper = wrapper
        self.vitessemax = vitessemax
        self.stopstrat = False
        self.stratTourner = StrategieTournerIRL.StrategieTournerIRL(wrapper, 5., 5.)

    def start(self):
        self.wrapper.RobotIRL.stop()
        self.stratTourner.start()

    def step(self):
        while not self.stop():
            if self.wrapper.get_distance() < 0.5:
                self.wrapper._vitesse = self.wrapper._vitesse // 2
                time.sleep(0.1)
                self.wrapper._vitesse = 0
                angleTourne = 0.
                while self.wrapper.get_ditance() < 0.5:
                    if angleTourne >= 360:
                        self.stopstrat = True
                        break
                    self.stratTourner.step()
                    angleTourne += 5
            else:
                self.wrapper._vitesse = self.vitessemax

    def stop():
        if self.stopstrat:
            self.wrapper.RobotIRL.stop()
        return self.stopstrat
