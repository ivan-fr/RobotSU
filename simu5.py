from views import Terrain
from models import TerrainContinu, Robot, Polygone, Wrapper, RobotIRLInterface
from controllers import StrategieCarre
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


def updateStrats(stratCarre, fps):
    while not stratCarre.stop():
        stratCarre.step()
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
    robot = Robot.Robot(-3, -3, 0., 0.)
    wrapper = Wrapper.Wrapper(RobotIRLInterface.RobotIRLInterface())
    # mache avec 90 ou -90 comme valeur de rotation, entier positif pour distance
    stratCarre = StrategieCarre.StrategieCarre(wrapper, robot, 3., 2., 7.)
    # --> pour pouvoir faire des carres dans des sens differents
    stratCarre.start()

    fps = 60

    t1 = threading.Thread(target=affichage, args=(robot, tc, fps))
    t2 = threading.Thread(target=updateStrats, args=(stratCarre, fps))
    t3 = threading.Thread(target=updateRobot, args=(robot, tc, fps))
    t1.start()
    t2.start()
    t3.start()


if __name__ == '__main__':
    run()
