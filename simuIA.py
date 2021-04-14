from views import Terrain
from models import Robot, Polygone, Wrapper
from controllers import StrategieIA
import threading
import time

try:
    from robot2I013 import Robot2I013
except: 
    from models.RobotIRLInterface import RobotIRLInterface as Robot2I013

stop_thread = True

def updateStrats(stratIA, fps):
    stratIA.start()
    while not stratIA.stop():
        stratIA.step()
        time.sleep(1./fps)
    global stop_thread
    stop_thread = False

def run():
    wrapper = Wrapper.Wrapper(Robot2I013())
    stratIA = StrategieIA.StrategieIA(wrapper, 70.)
    fps = 60

    t2 = threading.Thread(target=updateStrats, args=(stratIA, fps))
    t2.start()


if __name__ == '__main__':
    run()
