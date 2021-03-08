from controllers import StrategieAvancerDroit, StrategieTourner

class StrategieAvancerDroitMax(object):
    def __init__(self,terrainC):
        self.tc = terrainC
        self.tc.robot.etat = None
        self.stratAvancer = StrategieAvancerDroit.StrategieAvancerDroit(2000, 1, self.tc)
        


    def start(self):
        self.stratAvancer.start()

    def step(self):
        x = self.stratAvancer.tc.robot.pos_x 
        y = self.stratAvancer.tc.robot.pos_y 
        if not self.stratAvancer.tc.collision((x,y),self.stratAvancer.tc.robot.vecteurDeplacement):
            self.stratAvancer.step()
        else :
            print("le robot s'est approché le plus possible du mur")
    
