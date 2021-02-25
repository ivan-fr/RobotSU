from models import Robot

class StrategieTourner(object) :

    def __init__(self, rotationAngle, robot):
        self.robot = robot
        self.angle = self.robot.angle
        self.rotationAngle = rotationAngle

    def start(self):
        self.step()

    def step(self):
        if self.stop() : return 
        print(self.robot.angle)
        self.robot.rotation(self.rotationAngle)
        self.angle = self.robot.angle

    def stop(self):
        return self.robot.angle >= self.angle+self.rotationAngle