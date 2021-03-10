from models import Robot

class StrategieTourner(object) :

    def __init__(self, rotationAngle, robot):
        self.robot = robot
        self.rotationAngle = rotationAngle

    def start(self):
        self.newA = (self.robot.angle+self.rotationAngle) % 360.

        if self.newA > 180.:
            self.newA -= 360.

    def step(self):
        self.robot.rotation(self.rotationAngle)

    def stop(self):
        # condition d'arret, si le robot a bien tourne de l'angle demande  
        return abs(self.robot.angle - self.newA) <= 0.5
