from controllers import StrategieAvancerDroit, StrategieTourner

class StrategieCarre(object):
    def __init__(self,terrainC, coteCarre):
        self.tc = terrainC
        self.tc.robot.etat = None
        self.stratAvancer = StrategieAvancerDroit.StrategieAvancerDroit(coteCarre, 1, self.tc)
        self.stratTourner = StrategieTourner.StrategieTourner(90., self.tc)
        
        self.nbCoteParcouru = 0
        self.stop = False

    def start(self):
        self.nbCoteParcouru = 0
        self.stratAvancer.start()
        self.stratTourner.start()
        self.stop = False

    def step(self):
        if not self.stratAvancer.stop():
            self.stratAvancer.step()
        elif not self.stratTourner.stop:
            self.stratTourner.step()
        
        if self.stratTourner.stop and self.stratAvancer.stop():
            self.nbCoteParcouru += 1

            if self.nbCoteParcouru == 4:
                self.stop = True
            else:
                self.stratAvancer.start()
                self.stratTourner.start()
