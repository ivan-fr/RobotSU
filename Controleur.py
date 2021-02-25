import StrategieTourner
import StrategieAvancerDroit

class Controleur(object):
    def __init__(self,Robot,terrainC):
        self.robot = Robot
        self.robot.etat = None
        self.stratAvancer = StrategieAvancerDroit.StrategieAvancerDroit(3,1, self.robot, terrainC)
        self.stratTourner = StrategieTourner.StrategieTourner(90,self.robot)

    def update(self):
        if self.robot.etat == None or self.robot.etat == "tourner" :
            self.stratAvancer.start()
            self.robot.etat = "avancer"
        else :
            self.stratTourner.start()
            self.robot.etat = "tourner"
