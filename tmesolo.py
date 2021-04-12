from views import Terrain
from models import TerrainContinu, Robot, Polygone, Wrapper
from controllers import StrategieTournerIRL, StrategieAvancerDroitIRL
import threading
import time
import datetime

try:
    from robot2I013 import Robot2I013
except: 
    from models.RobotIRLInterface import RobotIRLInterface as Robot2I013

stop_thread = True

def updateStrats(stratAvancer, fps):
    stratAvancer.start()
    while not stratAvancer.stop():
        stratAvancer.step()
        time.sleep(1./fps)
    global stop_thread
    stop_thread = False

def pointilier(wrapper):
    while stop_thread:
        wrapper.robotIRL.down()
        time.sleep(1)
        wrapper.robotIRL.up()

def q1_1(wrapper):
    startAvancer = StrategieAvancerDroitIRL.StrategieAvancerDroitIRL(wrapper, 70., 15.)

    fps = 60

    t2 = threading.Thread(target=updateStrats, args=(startAvancer, fps))
    t2.start()

def q1_2(wrapper):
    startAvancer = StrategieAvancerDroitIRL(wrapper, 70., 15.)

    fps = 60
    t2 = threading.Thread(target=updateStrats, args=(startAvancer, fps))
    t3 = threading.Thread(target=pointilier, args=(wrapper,))
    t3.start()
    t2.start()


class StrategieTriangleEq(object):
    def __init__(self, stratAvancer):
        self.liste_strategies = [stratAvancer, StrategieTournerIRL.StrategieTournerIRL(stratAvancer.wrapper, 120., 30.)] * 3
        self.i_liste_strategies = 0

    def start(self):
        self.i_liste_strategies = 0
        self.liste_strategies[self.i_liste_strategies].start()

    def step(self):
        if self.stop():
            return

        if not self.liste_strategies[self.i_liste_strategies].stop():
            self.liste_strategies[self.i_liste_strategies].step()
        else:
            self.i_liste_strategies += 1
            if self.stop():
                return
            else:
                self.liste_strategies[self.i_liste_strategies].start()

def q2_1(wrapper):
    startAvancer = StrategieAvancerDroitIRL.StrategieAvancerDroitIRL(wrapper, 70., 15.)
    stratBalise = StrategieTriangleEq(startAvancer, startTourner)

    fps = 60

    t2 = threading.Thread(target=updateStrats, args=(stratBalise, fps))
    t2.start()

if __name__ == '__main__':
    # q1_1(Wrapper.Wrapper(Robot2I013()))
    q1_2(Wrapper.Wrapper(Robot2I013()))
