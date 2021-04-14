from views import Terrain
from models import Robot, Polygone, Wrapper
from controllers import StrategieSuivreBalise, StrategieAvancerDroitIRL, StrategieTournerIRL
import threading
import time

try:
    from robot2I013 import Robot2I013
except: 
    from models.RobotIRLInterface import RobotIRLInterface as Robot2I013

stop_thread = True

def updateStrats(stratBalise, fps):
    stratBalise.start()
    while not stratBalise.stop():
        stratBalise.step()
        time.sleep(1./fps)
    global stop_thread
    stop_thread = False

def run():
    wrapper = Wrapper.Wrapper(Robot2I013())
    startAvancer = StrategieAvancerDroitIRL.StrategieAvancerDroitIRL(wrapper, 70., 15.)
    startTourner = StrategieTournerIRL.StrategieTournerIRL(wrapper, 40., 20.)
    stratBalise = StrategieSuivreBalise.StrategieSuivreBalise(startAvancer, startTourner)

    fps = 60

    t2 = threading.Thread(target=updateStrats, args=(stratBalise, fps))
    t2.start()


if __name__ == '__main__':
    run()
