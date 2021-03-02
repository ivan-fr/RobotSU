from models import Robot

class StrategieTourner(object) :

    def __init__(self, rotationAngle, tc):
        self.tc = tc
        self.rotationAngle = rotationAngle
        self.stop = False

    def start(self):
        self.stop = False

    def step(self):
        self.tc.robot.rotation(self.rotationAngle)
        self.stop = True
