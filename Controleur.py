import StrategieTourner
import StrategieAvancerDroit

class Controleur(object):
    def __init__(self,Robot,terrainC, rotation, distance):
        self.robot = Robot
        self.rotation = rotation
        self.tc = terrainC
        self.robot.etat = None
        self.distance = distance
        self.stratAvancer = StrategieAvancerDroit.StrategieAvancerDroit(self.distance,1, self.robot, self.tc)
        self.stratTourner = StrategieTourner.StrategieTourner(self.rotation,self.robot, self.tc)

    def update(self):
        if self.tc.robot.etat == None or self.tc.robot.etat == "tourner" :
            self.stratAvancer.start()
            while self.stratAvancer.stop() :
                self.stratAvancer.step()
            #on garde en memoire quelle strategy on vient d'effectuer
            self.tc.robot.etat = "avancer"
        else :
            self.stratTourner.start()
            #on garde en memoire quelle strategy on vient d'effectuer
            self.tc.robot.etat = "tourner"