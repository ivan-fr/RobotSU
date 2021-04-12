from views import Terrain
from models import TerrainContinu, Robot, Polygone, Wrapper, RobotIRLInterface
from controllers import StrategieAvancerDroit, StrategieTourner
import threading
import time

class StrategieTriangle(object):
    def __init__(self, stratAvancer, stratTourner):
        self.liste_strategies = [stratAvancer, stratTourner] * 3
        self.i_liste_strategies = 0

    def start(self):
        self.liste_strategies[self.i_liste_strategies].start()

    def step(self):
        if self.stop():
            return

        if not self.liste_strategies[self.i_liste_strategies].stop():
            self.liste_strategies[self.i_liste_strategies].step()
        
        if self.liste_strategies[self.i_liste_strategies].stop():
            self.i_liste_strategies += 1
            if self.stop():
                return
            else:
                self.start()

    def stop(self):
        #condition d'arret lorsque le robot a parcouru les 3 cotes
        try:
            _ = self.liste_strategies[self.i_liste_strategies]
            return False
        except IndexError:
            return True




