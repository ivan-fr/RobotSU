import unittest
import random
from models import Polygone, Vecteur


class PolygoneTest(unittest.TestCase):
    def is_polygone(self, polygone):
        v = Vecteur.Vecteur(0., 0.)

        for vp in polygone.liste_vecteur:
            v = v + vp

        self.assertTrue(abs(v.x) <= 0.00001 and abs(v.y) <= 0.00001)

    def test_construct_polygone(self):
        liste_sommets = []

        for _ in range(20):
            liste_sommets.append(
                (random.uniform(10., 50.), random.uniform(10., 50.)))

        po = Polygone.Polygone(liste_sommets)

        self.is_polygone(po)

    def test_collision(self):
        """tuple(int * int) *  Vecteur -> boolean
        methode qui verifie la collision du robot avec un objet.
        """

        liste_sommets = []

        for _ in range(20):
            liste_sommets.append(
                (random.uniform(10., 50.), random.uniform(10., 50.)))

        p = Polygone.Polygone(liste_sommets)
        posRobot = (random.uniform(10., 50.), random.uniform(10., 50.))
        vD = Vecteur.Vecteur(random.uniform(10., 50.),
                             random.uniform(10., 50.))

        bo = False
        i = 0
        while i < len(p._liste_sommet):
            if p.liste_vecteur[i].collision(p._liste_sommet[i], vD, posRobot):
                bo = True
                break
            i = i + 1

        self.assertTrue(bo == p.collision(posRobot, vD))

    def test_Carre(self):
        self.is_polygone(Polygone.Carre(
            (random.uniform(10, 100), random.uniform(10, 100)), random.uniform(10, 100)))

    def test_Triangle(self):
        self.is_polygone(Polygone.Triangle(
            (random.uniform(10, 100), random.uniform(10, 100)), random.uniform(10, 100)))

    def test_hexagone(self):
        self.is_polygone(Polygone.hexagone(
            (random.uniform(10, 100), random.uniform(10, 100)), random.uniform(10, 100)))
