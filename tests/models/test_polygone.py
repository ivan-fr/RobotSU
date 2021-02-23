import unittest
import random
from models import Polygone, Vecteur

class PolygoneTest(unittest.TestCase):
    def test_construct_polygone(self):
        liste_sommets = []

        for _ in range(20):
            liste_sommets.append((random.uniform(10.,50.), random.uniform(10.,50.)))

        p = Polygone.Polygone(liste_sommets)

        v = Vecteur.Vecteur(0.,0.)

        for vp in p.liste_vecteur:
            v = v + vp

        self.assertTrue(abs(v.x) <= 0.00001 and abs(v.y) <= 0.00001)