import random
from models import Wrapper, RobotIRL, Vecteur
import math
import unittest

class WrapperTest(unittest.TestCase):
    def test_contruct_Wrapper(self):
        rIRL = RobotIRL.RobotIRL(None)
        w = Wrapper.Wrapper(rIRL)

        self.assertTrue(w.RobotIRL == rIRL)
        self.assertTrue(w._vitesse == 0)
        self.assertTrue(w._degreParSeconde == 0)
        self.assertIsNone(w._vecteurDeplacement)
        self.assertTrue(w.bouger == 0)

    def test_vecteurDeplacement(self):
        w = Wrapper.Wrapper(rIRL)
        vecteurDeplacement_x = random.randint(-500,500)
        vecteurDeplacement = Vecteur.Vecteur(random.randint(-500,500),random.randint(-500,500))
        w.vecteurDeplacement(vecteurDeplacement)

        VecteurToAngle = Wrapper.fromVecteurToAngle(vecteurDeplacement)

        self.assertTrue(w._vecteurDeplacement == vecteurDeplacement)
        self.assertTrue(VecteurToAngle.x == vecteurDeplacement.x)
        self.assertTrue(VecteurToAngle.y == vecteurDeplacement.y)
        self.assertTrue(w._degreParSeconde == VecteurToAngle)

