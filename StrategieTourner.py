from models import Robot

class StrategieTourner(object) :

    def __init__(self, rotationAngle, robot, tc):
        self.tc = tc
        self.robot = robot
        self.angle = self.tc.robot.angle
        self.rotationAngle = rotationAngle

    def start(self):
        self.angle = self.tc.robot.angle
        self.step()

    def step(self):
        self.tc.robot.rotation(self.rotationAngle)