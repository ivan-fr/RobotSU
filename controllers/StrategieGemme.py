from models import Robot
from controllers import StrategieTourner, StrategieAvancerDroit

class StrategieGemme(object):
    def __init__(self, Robot, vitesse):
        self.robot = Robot
        self.vitesse = vitesse

    def start(self):
        self.nbgemmes = 0
        self.lastUpdate
        self.stop = False

    def step(self, get_signal):
        distance = get_signal[0]
        angle = get_signal[1]
        stratTourner = StrategieTourner.StrategieTourner(angle, 2., self.robot)
        stratTourner.start()
        while not stratTourner.stop():
            stratTourner.step()
        stratAvancer = StrategieAvancerDroit.StrategieAvancerDroit(distance, self.vitesse, self.robot)
        stratAvancer.start()
        while not stratTourner.stop():
            stratTourner.step()

    def stop():
        if self.stop:
            self.robot.vitesse = 0
        return self.stop