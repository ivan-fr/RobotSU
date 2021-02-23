from models import Robot

class StrategieTourner :

    def __init__(self, rotationAngle, robot):
        self.robot = robot
        self.rotationAngle = rotationAngle
        self.temps = temps

    def start(self):
        self.robot.angle = 0

    def step(self):
        if self.stop() : return 
        self.robot.rotation(self.rotationAngle)

    def stop(self):
        return self.rotationAngle > self.distance