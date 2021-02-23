import random
from models import Robot
# from math import cos, sin, radians
import math
import unittest

class TestRobot (unittest.TestCase):

    def setUp(self):
        # premier robot : r et ses attributs
        self.x = random.uniform(-50, 50)
        self.random_x = random.randint(0, 50)
        self.random_y = random.randint(0, 50)
        self.random_vitesse = random.uniform(-50, 50)
        self.random_angle = random.uniform(-180, 180)
        self.r = Robot.Robot(self.random_x, self.random_y, self.random_vitesse, self.random_angle)
        # deuxieme robot : Robot et ses attributs
        self.vitesse = random.uniform(-10, 10)
        self.angle = random.uniform(-180, 180)
        self.pos_x_init = random.uniform(-50, 50)
        self.pos_y_init = random.uniform(-50, 50)
        self.temps = random.randint(1, 100)
        self.Robot = Robot.Robot(self.pos_x_init, self.pos_y_init, self.vitesse, self.angle)
        # troisieme robot : rimmob
        self.rimmob = Robot.Robot(self.pos_x_init, self.pos_y_init, 0., self.angle)

    def testRob(self):
        #test premier robot
        self.assertEqual(self.r.x,self.random_x)
        self.assertEqual(self.r.y,self.random_y)
        self.assertEqual(self.r.vitesse,self.random_vitesse)
        self.assertEqual(self.r.angle,self.random_angle)
        #test deuxieme robot
        self.assertEqual(self.Robot.x,self.pos_x_init)
        self.assertEqual(self.Robot.y,self.pos_y_init)
        self.assertEqual(self.Robot.vitesse,self.vitesse)
        self.assertEqual(self.Robot.angle,self.angle)

    def testRotation(self):
        rr = Robot.Robot(0.,0.,1.,0.)
        oldAngle = rr.angle
        oldVecteurD = rr.vecteurDeplacement
        randomAngleRelative = random.uniform(-180, 180)
        rr.rotation(randomAngleRelative)

        oldAngle += randomAngleRelative
        oldAngle %= 360

        if oldAngle > 180.:
            oldAngle -= 360

        self.assertLess(abs(oldAngle-rr.angle),0.0001)

        compare_vecteur = rr.vecteurDeplacement + oldVecteurD.rotation(randomAngleRelative) * (-1)
        self.assertLess(abs(compare_vecteur.norme()), 0.00001)
    
    def test_setter_vitesse(self):
        self.r.vitesse = self.x
        self.assertEqual(self.r.vecteurDeplacement.x, math.cos(math.radians(self.r.angle)) * self.r.vitesse)
        self.assertEqual(self.r.vecteurDeplacement.y, math.sin(math.radians(self.r.angle)) * self.r.vitesse)

    def test_avance(self):
        # cas particuliers d'immobilité

        # cas d'une vitesse nulle => immobile
        self.rimmob.avance(self.temps)
        self.assertEqual(self.rimmob.x, self.pos_x_init)
        self.assertEqual(self.rimmob.y, self.pos_y_init)
        # cas d'un temps null => immobile
        self.Robot.avance(0)
        self.assertEqual(self.Robot.x, self.pos_x_init)
        self.assertEqual(self.Robot.y, self.pos_y_init)

        # cas général, en prenant en compte l'incertitude de calcul --> float (arrondis au 1e-10 pres)
        self.Robot.avance(self.temps)
        pos_x_fin = self.pos_x_init + ((math.cos(math.radians(self.angle)) * self.vitesse) * self.temps)
        pos_y_fin = self.pos_y_init + ((math.sin(math.radians(self.angle)) * self.vitesse) * self.temps)
        # ordre de grandeur de l'incertitude = 0,0000000001 prés
        ordre_grandeur = 10 ** -10
        self.assertLess(abs(self.Robot.x - pos_x_fin),ordre_grandeur)  # test que valeurs identiques a 1e-10 prés
        self.assertLess(abs(self.Robot.y - pos_y_fin),ordre_grandeur)  # test que valeurs identiques a 1e-10 prés

if __name__ == '__main__':
    unittest.main()