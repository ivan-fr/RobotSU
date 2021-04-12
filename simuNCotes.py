from views import Terrain
from models import TerrainContinu, Robot, Polygone
from controllers import StrategieNCotes, StrategieAvancerDroit, StrategieTourner
import threading
import time
import math

stop_thread = True

def affichage(robot, tc, fps):
    while stop_thread:
        t = Terrain.construireTerrain(tc, robot)
        t.affichage()
        time.sleep(1./fps)
        t.supprimerAffichage()

def updateStrats(stratNCotes, fps):
    stratNCotes.start()
    while not stratNCotes.stop():
        stratNCotes.step()
        time.sleep(1./fps)
    global stop_thread
    stop_thread = False

def run():
    tc = TerrainContinu.Carre(20)
    #Robot = Robot.Robot(0,0)
    startAvancer = StrategieAvancerDroit.StrategieAvancerDroit(10., 70., Robot)
    startTourner = StrategieTourner.StrategieTourner(6*math.pi, 90., Robot)
    stratNCotes = StrategieNCotes.StrategieNCotes(startAvancer, startTourner, 8)

    fps = 60
    t1 = threading.Thread(target=affichage, args=(Robot, tc, fps))
    t2 = threading.Thread(target=updateStrats, args=(stratNCotes, fps))
    t2.start()


if __name__ == '__main__':
    run()
