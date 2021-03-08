from views import Terrain
from models import TerrainContinu, Robot, Polygone
from controllers import StrategieCarre
import threading
import time
import curses

stop_thread = True


def affichage(tc, fps):
    global stop_thread
    while stop_thread:
        t = Terrain.construireTerrain(tc, 0.5)
        t.affichage()
        time.sleep(1./fps)
        t.supprimerAffichage()


def updateStrats(stratCarre, fps):
    while not stratCarre.stop():
        stratCarre.step()
        time.sleep(1./fps)
    stop_thread = False
    print(stop_thread)


def updateTerrainContinu(tc, fps):
    global stop_thread
    while stop_thread:
        tc.update()
        time.sleep(1./fps)


def run():
    tc = TerrainContinu.Carre(20)
    tc.robot = Robot.Robot(0, 0, 0., 0.)
    # mache avec 0 ou 180
    tc.robot.rotation(0)
    # mache avec 90 ou -90 comme valeur de rotation, entier positif pour distance
    stratCarre = StrategieCarre.StrategieCarre(tc, 7.)
    # --> pour pouvoir faire des carres dans des sens differents
    stratCarre.start()

    fps = 60

    t1 = threading.Thread(target=affichage, args=(tc, fps))
    t2 = threading.Thread(target=updateStrats, args=(stratCarre, fps))
    t3 = threading.Thread(target=updateTerrainContinu, args=(tc, fps))
    t1.start()
    t2.start()
    t3.start()
    print(stratCarre.stop())
    while(stratCarre.stop() == False):
        time.sleep(1)
    global stop_thread
    stop_thread = False


if __name__ == '__main__':
    run()
