from views import Terrain
from models import TerrainContinu, Robot, Polygone
from controllers import StrategieAvancerDroitMax
import threading
import time
import curses

stop_thread = True


def affichage(robot, tc, fps):
    while stop_thread:
        t = Terrain.construireTerrain(tc, robot, 0.5)
        t.affichage()
        time.sleep(1./fps)
        t.supprimerAffichage()


def updateStrats(stratAvance, fps):
    while not stratAvance.stop():
        stratAvance.step()
        time.sleep(1./fps)
    global stop_thread
    stop_thread = False
    print(stop_thread)


def updateRobot(robot, tc, fps):
    while stop_thread:
        robot.update(tc)
        time.sleep(1./fps)


def run():
    tc = TerrainContinu.Carre(20)
    robot = Robot.Robot(0, 0, 0., 0.)
    # mache avec 90 ou -90 comme valeur de rotation, entier positif pour distance
    stratAvance = StrategieAvancerDroitMax.StrategieAvancerDroitMax(robot, 7., tc)
    # --> pour pouvoir faire des carres dans des sens differents
    stratAvance.start()

    fps = 60

    t1 = threading.Thread(target=affichage, args=(robot, tc, fps))
    t2 = threading.Thread(target=updateStrats, args=(stratAvance, fps))
    t3 = threading.Thread(target=updateRobot, args=(robot, tc, fps))
    t1.start()
    t2.start()
    t3.start()


if __name__ == '__main__':
    run()