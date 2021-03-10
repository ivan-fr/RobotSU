from controllers import StrategieAvancerDroit, StrategieTourner

class StrategieCarre(object):
    def __init__(self,robot, vitesse, degreParSeconde, coteCarre):
        self.robot = robot
        self.stratAvancer = StrategieAvancerDroit.StrategieAvancerDroit(coteCarre, vitesse, robot)
        self.stratTourner = StrategieTourner.StrategieTourner(90., 20., robot)
        
        self.nbCoteParcouru = 0

    def start(self):
        self.nbCoteParcouru = 0
        self.stratAvancer.start()
        self.stratTourner.start()

    def step(self):
        if not self.stratAvancer.stop():
            self.stratAvancer.step()
        elif not self.stratTourner.stop():
            self.stratTourner.step()
        
        if self.stratTourner.stop() and self.stratAvancer.stop():
            self.nbCoteParcouru += 1

            if self.nbCoteParcouru == 4:
                pass
            else:
                self.stratAvancer.start()
                self.stratTourner.start()
    
    def stop(self):
        #condition d'arret lorsque le robot a parcouru les 4 cotes
        return self.nbCoteParcouru == 4
