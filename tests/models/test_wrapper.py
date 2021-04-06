import random
from models import Wrapper, RobotIRLInterface, Vecteur
import math
import unittest

class WrapperTest(unittest.TestCase):
    def test_contruct_Wrapper(self):
        rIRL = RobotIRLInterface.RobotIRLInterface(None)
        w = Wrapper.Wrapper(rIRL)

        self.assertTrue(w.RobotIRL == rIRL)
        self.assertTrue(w._vitesse == 0)
        self.assertTrue(w.rayon_roue == w.RobotIRL.WHEEL_DIAMETER *10e-3 / 2.)
        self.assertTrue(w.rayon_robot == w.RobotIRL.WHEEL_BASE_WIDTH * 10e-3 / 2.)
        self.assertTrue(w.lastRotation == (None,None))

    def test_vitesse(self):
        vitesse = random.randint(0, 500)
        rIRL = RobotIRLInterface.RobotIRLInterface(None)
        w = Wrapper.Wrapper(rIRL)
        w._vitesse = vitesse
        self.assertTrue(w._vitesse == vitesse)

    def test_rotation(self):
        degreParSecondeVoulu = random.uniform(0, 50)
        vitesse = random.randint(0, 500)
        rIRL = RobotIRLInterface.RobotIRLInterface(None)
        w = Wrapper.Wrapper(rIRL)
        w._rotation = degreParSecondeVoulu
        self.assertTrue(w._rotation == degreParSecondeVoulu)

