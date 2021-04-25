from views import Terrain
from models import TerrainContinu, Robot, Polygone, Serializer
from controllers import StrategieAvancerDroit, StrategieTourner, StrategiePolygone
import threading
import time
import sys

stop_thread = True


def unity(robot, tc, fps):
    while stop_thread == True:
        Serializer.serialize(tc, robot)
        time.sleep(1./fps)


def updateStrats(stratavance, fps):
    stratavance.start()
    while not stratavance.stop():
        stratavance.step()
        time.sleep(1./fps)
    global stop_thread
    stop_thread = False


def updateRobot(robot, tc, fps):
    while stop_thread:
        robot.update(tc)
        time.sleep(1./fps)


def run(cote):
    tc = TerrainContinu.Carre(20)
    robot = Robot.Robot(-3, -3, 0., 0.)
    startAvancer = StrategieAvancerDroit.StrategieAvancerDroit(robot, 7., 15.)
    startTourner = StrategieTourner.StrategieTourner(robot, 0., 0.)
    stratPolygone = StrategiePolygone.StrategiePolygone(
        startAvancer, startTourner, int(cote))
    fps = 60

    t1 = threading.Thread(target=unity, args=(robot, tc, fps))
    t2 = threading.Thread(target=updateStrats, args=(stratPolygone, fps))
    t3 = threading.Thread(target=updateRobot, args=(robot, tc, fps))
    t1.start()
    t2.start()
    t3.start()


if __name__ == '__main__':
    run(sys.argv[1])
