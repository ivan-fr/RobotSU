import random
from models import Vecteur
# from math import cos, sin, radians
import math
import unittest


class TestVecteur(unittest.TestCase):

    def setUp(self):
        self.v1 = Vecteur.Vecteur(4, 7)
        self.v2 = Vecteur.Vecteur(7, -3)

    def testVect(self):
        self.assertEqual(self.v1.x, 4)
        self.assertEqual(self.v1.y, 7)
        self.assertEqual(self.v2.x, 7)
        self.assertEqual(self.v2.y, -3)

    def test_add(self):
        v = self.v1.__add__(self.v1)
        self.assertEqual(v.x, 8)
        self.assertEqual(v.y, 14)

    def test_mult(self):
        alea_int = random.randint(-500, 500)
        v = self.v1.__mul__(alea_int)
        self.assertEqual(v.x, self.v1.x * alea_int)
        self.assertEqual(v.y, self.v1.y * alea_int)

    def test_prod_VectScal(self):
        alea_int = random.randint(-500, 500)
        v = self.v1.__mul__(alea_int)
        self.assertEqual(v.x, 4 * alea_int)
        alea_float = random.uniform(-500, 500)
        vv = self.v2.__mul__(alea_float)
        self.assertEqual(vv.x, 7 * alea_float)

    def test_norme(self):
        aleaX = random.randint(-100, 100)
        aleaY = random.randint(-100, 100)
        v = Vecteur.Vecteur(aleaX, aleaY)
        self.assertEqual(v.x, aleaX)
        self.assertEqual(v.y, aleaY)
        # self.assertIsInstance(v,Vecteur)
        # self.assertIsInstance(v,(int,int))

    def test_rotation(self):
        rx = random.randint(-50, 50)
        ry = random.randint(-50, 50)
        v = Vecteur.Vecteur(rx, ry)
        angle = random.uniform(-180, 180)
        v = v.rotation(angle)
        vx = rx * math.cos(math.radians(angle)) - ry * math.sin(math.radians(angle))
        vy = rx * math.sin(math.radians(angle)) + ry * math.cos(math.radians(angle))
        self.assertLessEqual(abs(v.x - vx), 0.00001)
        self.assertLessEqual(abs(v.y - vy), 0.00001)

    def test_Sym_XVecteur(self):
        rx = random.randint(-50, 50)
        ry = random.randint(-50, 50)
        v1 = Vecteur.Vecteur(rx, ry)
        v2 = v1.get_sym_x_axis()
        v3 = v1 + v2
        self.assertEqual(v1.norme(), v2.norme())
        self.assertEqual(v1.x, v2.x)
        self.assertEqual(v3.x, 2 * v1.x)
        self.assertEqual(v3.y, 0)


if __name__ == '__main__':
    unittest.main()
