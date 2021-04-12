from views import Terrain
from models import TerrainContinu, Robot, Polygone, Wrapper, RobotIRLInterface
from controllers import StrategieCarre, StrategieAvancerDroit, StrategieTourner
import threading
import time

stop_thread = True


def affichage(robot, tc, fps):
    while stop_thread:
        t = Terrain.construireTerrain(tc, robot)
        t.affichage()
        time.sleep(1./fps)
        t.supprimerAffichage()


def updateStrats(startAvancer, fps):
    startAvancer.start()
    while not startAvancer.stop():
        startAvancer.step()
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
    robot.down()
    startAvancer = StrategieAvancerDroit.StrategieAvancerDroit(10., 30., robot)
    fps = 60

    t1 = threading.Thread(target=affichage, args=(robot, tc, fps))
    t2 = threading.Thread(target=updateStrats, args=(startAvancer, fps))
    t3 = threading.Thread(target=updateRobot, args=(robot, tc, fps))
    t1.start()
    t2.start()
    t3.start()


if __name__ == '__main__':
    run()
