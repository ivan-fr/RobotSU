import unittest
import random
from models import TerrainContinu, Robot, Polygone, Vecteur

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

    def test_collision(self):
        """tuple (int * int) * Vecteur -> boolean
        méthode qui verifie la collision du robot avec les objets contenu sur le terrain ainsi qu'avec 
        les vecteurs qui le delimitent
        : param tuple : coordonnees du robot
        : param Vecteur : vecteur de deplacement du robot
        """

        tc = TerrainContinu.Carre(20, (1.,1.))
        tc.ajoutPolygone(Polygone.Carre((10.,10.), 5))

        posOrigine = (3.,3.)
        vecteurDeplacement = Vecteur.Vecteur(random.uniform(20.,20.), random.uniform(20.,20.))

        b = False
        for p in tc.listePolygone:
            if p.collision(posOrigine, vecteurDeplacement):
                b = True
        # posX, posY : position du premier vecteur du terrain
        posX = 0.
        posY = 0.
        for v in tc.vecteursSurface:
            # vecteurDeplacement et (x,y) du robot
            if (v.collision((posX, posY), vecteurDeplacement, posOrigine)):
                b = True
            # calcul de l'origine des vecteurs suivants
            posX = posX + v.x
            posY = posY + v.y

        self.assertTrue(b == tc.collision(posOrigine, vecteurDeplacement))
