from models import Robot

class StrategieTourner(object) :

    def __init__(self, rotationAngle, tc):
        self.tc = tc
        self.rotationAngle = rotationAngle
        self.ancienAngle = self.tc.angle

    def start(self):
        self.ancienAngle = self.tc.angle

    def step(self):
        self.tc.robot.rotation(self.rotationAngle)

    def stop(self):
        # condition d'arret, si le robot a bien tourne de l'angle demande  
        return self.tc.robot.angle >= self.ancienAngle+self.rotationAngle