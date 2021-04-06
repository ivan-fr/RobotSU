from views import Terrain
from models import TerrainContinu, Robot, Polygone, Wrapper
from controllers import StrategieAvancerDroitMaxIRL
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
    tc = TerrainContinu.Carre(20)
    wrapper = Wrapper.Wrapper(Robot2I013())
    vitessemax = 500
    stratADM = StrategieAvancerDroitMaxIRL.StrategieAvancerDroitMaxIRL(wrapper,vitessemax,tc,lastUpdate=None)

    fps = 60

    t2 = threading.Thread(target=updateStrats, args=(stratADM, fps))
    t2.start()


if __name__ == '__main__':
    run()
