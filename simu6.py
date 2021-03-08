from views import Terrain
from models import TerrainContinu, Robot, Polygone
from controllers import StrategieAvancerDroitMax
import threading
import time
import curses


def affichage(tc, fps):
    while True:
        t = Terrain.construireTerrain(tc, 0.5)
        t.affichage()
        time.sleep(1./fps)
        t.supprimerAffichage()


def updateStrats(stratavance, fps, stop):
    while not stratavance.stop:
        stratavance.step()
        print("running")
        if stop:
            break


def updateTerrainContinu(tc, fps):
    while True:
        tc.update()
        time.sleep(1./fps)


def run():
    tc = TerrainContinu.Carre(20)
    tc.robot = Robot.Robot(0, 0, 0., 0.)
    tc.robot.rotation(0)
    stratavance = StrategieAvancerDroitMax.StrategieAvancerDroitMax(tc)
    stratavance.start()

    fps = 24

    t1 = threading.Thread(target=affichage, args=(tc, fps))
    t2 = threading.Thread(target=updateStrats, args=(stratavance, fps))
    t3 = threading.Thread(target=updateTerrainContinu, args=(tc, fps))

    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    print('threads killed')


if __name__ == '__main__':
    run()
