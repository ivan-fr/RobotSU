from models import Robot
from controllers import StrategieTourner, StrategieAvancerDroit
import datetime

stop_strat = False

class StrategieSuivreBalise(object):
    def __init__(self, robot, dps, vitesse, TerrainContinu, StratTourner, verifImage):
        self.robot = robot
        self.dps = dps
        self.vitesse = vitesse
        self.verifImage = verifImage
        self.tc = TerrainContinu
        
    def start(self):
        self.angleCible = None
        self.robot._degreParSeconde = self.dps
        self.angleApplique = 0.
        self.lastUpdate = None
        self.stratTourner = None
        self.stratAvancer = None
    
    def step(self):
        if(self.angleCible is not None):
            self.stratTourner = StrategieTourner(self.angleCible, self.dps, self.robot)
            while(not self.stratTourner.stop()):
                self.stratTourner.step()
            #on est dans la direction de la balise, maintenant il faut sen rapprocher
            distance = self.robot.getDistance(tc)
            self.stratAvancer = StrategieAvancerDroit(distance - 1, self.vitesse, self.robot)
            while(not self.stratAvancer.stop()):
                self.stratAvancer.step()
            global strop_strat
            stop_strat = True
        else:
            if(self.angleApplique >= 360):
                #il n y a pas de balise sur le terrain
                global stop_strat
                stop_strat = True
            #sinon on fait tourner le robot pour trouver la balise
            elif self.lastUpdate is None:
                self.lastUpdate = datetime.datetime.now()
            else:
                now = datetime.datetime.now()
                deltaT = (now - self.lastUpdate).total_seconds()
                self.lastUpdate = now
                self.angleApplique += deltaT * self.robot._degreParSeconde
                if(self.verifImage):
                    self.angleCible = self.angleApplique

    def stop(self):
        global stop_strat
        return stop_strat