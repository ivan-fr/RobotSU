import unittest
from models import TerrainContinu, Robot, Polygone

class TerrainContinuTest(unittest.TestCase):
    def test_contruct_tc(self):
        tc = TerrainContinu.Carre(20, (1.,1.))
        self.assertIsNotNone(tc.vecteursSurface)
        self.assertIsNotNone(tc.robot)
        self.assertIsNotNone(tc.listePolygone)

    def test_ajout_polygone(self):
        tc = TerrainContinu.Carre(20, (1.,1.))
        length = len(tc.listePolygone)
        p = Polygone.Polygone(((0.,1.),(1.,0), (4,2)))
        tc.ajoutPolygone(p)
        self.assertTrue(length + 1 == len(tc.listePolygone))