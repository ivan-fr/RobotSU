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

    def test_collision(self):
        """tuple(int * int) *  Vecteur -> boolean
        methode qui verifie la collision du robot avec un objet.
        """

        liste_sommets = []

        for _ in range(20):
            liste_sommets.append((random.uniform(10.,50.), random.uniform(10.,50.)))

        p = Polygone.Polygone(liste_sommets)
        posRobot = (random.uniform(10.,50.), random.uniform(10.,50.))
        vD = Vecteur.Vecteur(random.uniform(10.,50.), random.uniform(10.,50.))

        b = False
        i = 0
        while (i < len(p.liste_sommet)):
            if p.liste_vecteur[i].collision(p.liste_sommet[i], vD, posRobot):
                b = True
            i = i + 1

        self.assertTrue(b == p.collision(posRobot, vD))    
