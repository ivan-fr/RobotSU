from views import Terrain
from models import TerrainContinu, Robot, Polygone, Wrapper, RobotIRLInterface
from controllers import StrategieAvancerDroit, StrategieTourner
import StrategieTriangle
import threading
import time

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
    #angle de 60°
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
