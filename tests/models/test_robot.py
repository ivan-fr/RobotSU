import random
from models import Robot
import math
import unittest

class RobotTest(unittest.TestCase):
    def test_contruct_Robot(self):
        random_x = random.randint(0, 50)
        random_y = random.randint(0, 50)
        random_vitesse = random.uniform(-50, 50)
        random_angle = random.uniform(-180., 180.)
        r = Robot.Robot(random_x, random_y, random_vitesse, random_angle)

        self.assertTrue(r.x == random_x)
        self.assertTrue(r.y == random_y)
        self.assertTrue(r.vitesse == random_vitesse)
        self.assertTrue(abs(r.angle - random_angle) < 0.0001)


    def test_rotation(self):
        r = Robot.Robot(0., 0., 1., 0.)
        oldAngle = r.angle
        oldVecteurD = r.vecteurDeplacement
        randomAngleRelative = random.uniform(-180, 180)
        r.rotation(randomAngleRelative)

        oldAngle += randomAngleRelative
        oldAngle %= 360

        if oldAngle > 180.:
            oldAngle -= 360

        self.assertTrue(abs(oldAngle - r.angle) < 0.0001)

        compare_vecteur = r.vecteurDeplacement + oldVecteurD.rotation(randomAngleRelative) * (-1)
        self.assertTrue(abs(compare_vecteur.norme()) < 0.00001)


    def test_avance(self):
        # cas particuliers d'immobilité
        temps = random.randint(1, 100)
        pos_x_init = random.uniform(-50, 50)
        pos_y_init = random.uniform(-50, 50)
        vitesse = random.uniform(-10, 10)
        angle = random.uniform(-180, 180)
        # cas d'une vitesse nulle => immobile
        r = Robot.Robot(pos_x_init, pos_y_init, 0., angle)
        r.avance(temps)
        self.assertTrue(r.x == pos_x_init)
        self.assertTrue(r.y == pos_y_init)
        # cas d'un temps null => immobile
        r = Robot.Robot(pos_x_init, pos_y_init, vitesse, angle)
        r.avance(0)
        self.assertTrue(r.x == pos_x_init)
        self.assertTrue(r.y == pos_y_init)

        # cas général, en prenant en compte l'incertitude de calcul --> float (arrondis au 1e-10 pres)
        for _ in range(1000):
            temps = random.randint(1, 100)
            pos_x_init = random.uniform(-50, 50)
            pos_y_init = random.uniform(-50, 50)
            vitesse = random.uniform(-10, 10)
            angle = random.uniform(-180, 180)
            r = Robot.Robot(pos_x_init, pos_y_init, vitesse, angle)
            r.avance(temps)
            pos_x_fin = pos_x_init + ((math.cos(math.radians(angle)) * vitesse) * temps)
            pos_y_fin = pos_y_init + ((math.sin(math.radians(angle)) * vitesse) * temps)
            # ordre de grandeur de l'incertitude = 0,0000000001 prés
            ordre_grandeur = 10 ** -10
            self.assertTrue(abs(r.x - pos_x_fin) < ordre_grandeur)  # test que valeurs identiques a 1e-10 prés
            self.assertTrue(abs(r.y - pos_y_fin) < ordre_grandeur)  # test que valeurs identiques a 1e-10 prés


    def test_setter_vitesse(self):
        random_x = random.randint(0, 50)
        random_y = random.randint(0, 50)
        random_vitesse = random.uniform(-50, 50)
        random_angle = random.uniform(0, 360)
        r = Robot.Robot(random_x, random_y, random_vitesse, random_angle)

        for _ in range(1000):
            x = random.uniform(-50, 50)
            r.vitesse = x
            self.assertTrue(r.vecteurDeplacement.x == math.cos(math.radians(r.angle)) * r.vitesse)
            self.assertTrue(r.vecteurDeplacement.y == math.sin(math.radians(r.angle)) * r.vitesse)
