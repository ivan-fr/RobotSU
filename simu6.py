from views import Terrain
from models import TerrainContinu, Robot, Polygone, Wrapper, RobotIRLInterface
from controllers import StrategieCarre, StrategieAvancerDroitIRL, StrategieTournerIRL
import threading
import time

stop_thread = True

def updateStrats(stratCarre, fps):
    stratCarre.start()
    while not stratCarre.stop():
        stratCarre.step()
        time.sleep(1./fps)
    global stop_thread
    stop_thread = False

def run():
    tc = TerrainContinu.Carre(20)
    wrapper = Wrapper.Wrapper(RobotIRLInterface.RobotIRLInterface())
    startAvancer = StrategieAvancerDroitIRL.StrategieAvancerDroitIRL(wrapper, 70., 15.)
    startTourner = StrategieTournerIRL.StrategieTournerIRL(wrapper, 90., 20.)
    stratCarre = StrategieCarre.StrategieCarre(startAvancer, startTourner)

    fps = 60

    t2 = threading.Thread(target=updateStrats, args=(stratCarre, fps))
    t2.start()


if __name__ == '__main__':
    run()
