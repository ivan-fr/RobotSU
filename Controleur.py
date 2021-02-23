class Controleur(object):
    def __init__(self,Robot):
        self.robot = Robot
        self.last_x = self.robot.x

    def update(self):
        if(self.robot.x):
            StategieAvancerDroit(3,1)
        else:
            StategieTourner(90,robot)