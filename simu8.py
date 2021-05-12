from views import Terrain
from models import Robot, Polygone, Wrapper
from controllers import StrategieAvancerDroitMaxIRL2
import threading
import time
try:
    from robot2I013 import Robot2I013
except: 
    from models.RobotIRLInterface import RobotIRLInterface as Robot2I013

stop_thread = True

def updateStrats(stratADM, fps):
    stratADM.start()
    while not stratADM.stop():
        stratADM.step()
        time.sleep(1./fps)
    global stop_thread
    stop_thread = False

def run():
    wrapper = Wrapper.Wrapper(Robot2I013())
    vitessemax = 600.
    stratADM = StrategieAvancerDroitMaxIRL2.StrategieAvancerDroitMaxIRL2(wrapper,vitessemax,lastUpdate=None)

    fps = 60

    t2 = threading.Thread(target=updateStrats, args=(stratADM, fps))
    t2.start()


if __name__ == '__main__':
    run()
