from views import Terrain
from models import Robot, Polygone, TerrainContinu
from controllers import StrategieIASimule
import threading
import time

stop_thread = True

try:
    from robot2I013 import Robot2I013
except: 
    from models.RobotIRLInterface import RobotIRLInterface as Robot2I013

def affichage(robot, tc, fps):
    while stop_thread:
        t = Terrain.construireTerrain(tc, robot)
        t.affichage()
        time.sleep(1./fps)
        t.supprimerAffichage()

def updateStrats(stratIAS, fps):
    stratIAS.start()
    while not stratIAS.stop():
        stratIAS.step()
        time.sleep(1./fps)

def updateRobot(robot, tc, fps):
    while stop_thread:
        robot.update(tc)
        time.sleep(1./fps)

def run():
    tc = TerrainContinu.Carre(20)
    robot = Robot.Robot(-3, -3, 0., 0.)
    stratIAS = StrategieIASimule.StrategieIASimule(robot, 4.,tc)
    fps = 60

    t1 = threading.Thread(target=affichage, args=(robot, tc, fps))
    t2 = threading.Thread(target=updateStrats, args=(stratIAS, fps))
    t3 = threading.Thread(target=updateRobot, args=(robot, tc, fps))
    t1.start()
    t2.start()
    t3.start()



if __name__ == '__main__':
    run()
