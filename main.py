from controllers import StrategieCarre
from models import Wrapper, Robot
import threading
try:
    from robot2I013 import Robot2I013
except: 
    from models.RobotIRLInterface import RobotIRLInterface as Robot2I013
import time

stop_thread = True


def updateStrats(stratCarre, fps):
    while not stratCarre.stop():
        stratCarre.step()
        time.sleep(1./fps)
    global stop_thread
    stop_thread = False

if __name__ == '__main__':
    robot = Robot2I013()
    robotsim = Robot.Robot(-3, -3, 0., 0.)
    wrapper = Wrapper.Wrapper(robot)
    # mache avec 90 ou -90 comme valeur de rotation, entier positif pour distance
    stratCarre = StrategieCarre.StrategieCarre(wrapper, robotsim, 3., 2., 7.)
    # --> pour pouvoir faire des carres dans des sens differents
    stratCarre.start()
    fps = 60
    t2 = threading.Thread(target=updateStrats, args=(stratCarre, fps))
    t2.start()