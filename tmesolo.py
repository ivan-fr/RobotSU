from views import Terrain
from models import TerrainContinu, Robot, Polygone, Wrapper
from controllers import StrategieTournerIRL, StrategieAvancerDroitIRL, StrategieAvancerDroit, StrategieTourner
import threading
import time
import datetime
import math
from models import TerrainContinu

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
    startAvancer = StrategieAvancerDroitIRL.StrategieAvancerDroitIRL(wrapper, 70., 15.)

    fps = 60
    t2 = threading.Thread(target=updateStrats, args=(startAvancer, fps))
    t3 = threading.Thread(target=pointilier, args=(wrapper,))
    t3.start()
    t2.start()


class StrategieTriangleEq(object):
    def __init__(self, stratAvancer):
        # 120 degrés pour tourner
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

    def stop(self):
        #condition d'arret lorsque le robot a parcouru les 4 cotes
        try:
            _ = self.liste_strategies[self.i_liste_strategies]
            return False
        except IndexError:
            return True

def q2_1(wrapper):
    startAvancer = StrategieAvancerDroitIRL.StrategieAvancerDroitIRL(wrapper, 70., 15.)
    triangle = StrategieTriangleEq(startAvancer)

    fps = 60

    t2 = threading.Thread(target=updateStrats, args=(triangle, fps))
    t2.start()


class StrategiePolygoneReg(object):
    def __init__(self, stratAvancer, n):
        # 120 degrés pour tourner
        target = (n - 2) * math.pi / n
        dps = target * 0.3
        self.liste_strategies = [stratAvancer, StrategieTournerIRL.StrategieTournerIRL(stratAvancer.wrapper, target, dps)] * n
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

    def stop(self):
        #condition d'arret lorsque le robot a parcouru les 4 cotes
        try:
            _ = self.liste_strategies[self.i_liste_strategies]
            return False
        except IndexError:
            return True

def q2_2(wrapper):    
    startAvancer = StrategieAvancerDroitIRL.StrategieAvancerDroitIRL(wrapper, 70., 15.)
    polygone = StrategiePolygoneReg(startAvancer, 8)

    fps = 60

    t2 = threading.Thread(target=updateStrats, args=(polygone, fps))
    t2.start()


class Strategie5cmMur(object):
    def __init__(self, wrapper):
        self.wrapper = wrapper

    def start(self):
        self.wrapper.robotIRL.stop()

    def step(self):
        if self.stop():
            return
            
        if self.wrapper.vitesse < 10e-3:
            self.wrapper.vitesse = 10

    def stop(self):
        # condition d'arret, lorsque que le robot a parcourut la distance souhaitee ou qu'il a rencontre un obstacle
        result = self.wrapper.robotIRL.get_distance() * 10e-1 < 5.
        if result:            
            self.wrapper.vitesse = 0.
            self.wrapper.RobotIRL.stop()
        return result

class longerLeMur(object):
    def __init__(self, wrapper):
        self.strat5cm = Strategie5cmMur(wrapper)
        self.wrapper = wrapper
        self.tourner90 = StrategieTournerIRL.StrategieTournerIRL(wrapper, 90., 30.)
        self.i = -1

    def start(self):
        self.strat5cm.start()
        self.wrapper.robotIRL.stop()
        self.tourner90.start()

    def step(self):
        if self.stop():
            return

        if not self.strat5cm.stop():
            self.strat5cm.step()
        elif not self.tourner90.stop():
            self.tourner90.step()
        else:
            self.tourner90.start()
            self.strat5cm.start()
            self.i += 1

    def stop(self):
        return self.i == 4

def q2_3(wrapper):    
    longerMur = longerLeMur(wrapper)

    fps = 60

    t2 = threading.Thread(target=updateStrats, args=(longerMur, fps))
    t2.start()

def affichage(robot, tc, fps):
    while stop_thread:
        t = Terrain.construireTerrain(tc, robot)
        if tc.gemmes:
            print(robot.get_signal(tc.gemmes[0]))
        t.affichage()
        time.sleep(1./fps)
        t.supprimerAffichage()

def gemmes(tc):
    while stop_thread:
        tc.ajout_gemme()
        time.sleep(20)

def updateTC(tc, fps):
    while stop_thread:
        tc.gemmes_destroy()
        time.sleep(1./fps) 

class stratGemme(object):
    def __init__(self, robot):
        self.wrapper = robot
        self.avance = StrategieAvancerDroit.StrategieAvancerDroit(0., 15., wrapper)
        self.tourner = StrategieTourner.StrategieTourner(0., 30., wrapper)
        self.i = -1
        self.stat = False

    def start(self):
        self.avance.start()
        self.wrapper.robotIRL.stop()
        self.tourner.start()

    def step(self):
        if not self.stat:
            distance, angle = self.wrapper.get_signal()
            self.tourner.angleTarget = angle
            self.avance.distance = distance
            self.stat = True

        if not self.tourner.stop():
            self.tourner.step()
            self.tourner.angleTarget = 0
        elif not self.avance.stop():
            self.avance.step()            
            self.avance.distance = 0
        else:
            self.avance.start()
            self.tourner.start()
            self.stat = False

def q3_1():
    tc = TerrainContinu.Carre(20)
    robot = Robot.Robot(0, 0, 0., 0.)
    fps = 1
    t1 = threading.Thread(target=affichage, args=(robot, tc, fps))
    t2 = threading.Thread(target=gemmes, args=(tc,))
    t3 = threading.Thread(target=updateTC, args=(tc,fps))
    t1.start()
    t2.start()
    t3.start()

if __name__ == '__main__':
    # q1_1(Wrapper.Wrapper(Robot2I013()))
    q3_1()
