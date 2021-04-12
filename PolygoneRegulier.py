from views import Terrain
from models import TerrainContinu, Robot, Polygone, Wrapper, RobotIRLInterface
from controllers import StrategieAvancerDroit, StrategieTourner
import threading
import time
import datetime
import math

class StrategieTourner(object) :
    def __init__(self, nombreCotes, stratAvancer, robot):
        self.nbCotes = nombreCotes
        self.stratAvancer = stratAvancer
        self.angle = (self.nbCotes-2)*math.pi/self.nbCotes
        self.stratTourner = StrategieTourner.StrategieTourner(self.angle, 45, robot)

        self.liste_strategies = [stratAvancer, stratTourner] * nbCotes
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

stop_thread = True

def affichage(robot, tc, fps):
    while stop_thread:
        t = Terrain.construireTerrain(tc, robot)
        t.affichage()
        time.sleep(1./fps)
        t.supprimerAffichage()


def updateStrats(stratTriangle, fps):
    stratTriangle.start()
    while not stratTriangle.stop():
        stratTriangle.step()
        time.sleep(1./fps)
    global stop_thread
    stop_thread = False


def updateRobot(robot, tc, fps):
    while stop_thread:
        robot.update(tc)
        time.sleep(1./fps)


def run():
    tc = TerrainContinu.Carre(20)
    robot = Robot.Robot(-3, -3, 0., 0.)
    startAvancer = StrategieAvancerDroit.StrategieAvancerDroit(5., 30., robot)
    startTourner = StrategieTourner.StrategieTourner(60., 45., robot)
    stratTriangle = StrategieTriangle.StrategieTriangle(startAvancer, startTourner)

    fps = 60

    t1 = threading.Thread(target=affichage, args=(robot, tc, fps))
    t2 = threading.Thread(target=updateStrats, args=(stratTriangle, fps))
    t3 = threading.Thread(target=updateRobot, args=(robot, tc, fps))
    t1.start()
    t2.start()
    t3.start()


if __name__ == '__main__':
    run()