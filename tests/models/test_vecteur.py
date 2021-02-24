import random
from models import Vecteur
import math
import unittest

class VecteurTest(unittest.TestCase):
    def test_constructVecteur(self):
        random_x = random.randint(-500, 500)
        random_y = random.randint(-500, 500)
        V = Vecteur.Vecteur(random_x, random_y)

        self.assertTrue(V.x == random_x)
        self.assertTrue(V.y == random_y)


    def test__add__(self):
        for _ in range(1000):
            v1 = Vecteur.Vecteur(random.randint(-500, 500), random.randint(-500, 500))
            v2 = Vecteur.Vecteur(random.randint(-500, 500), random.randint(-500, 500))
            vv = v1.__add__(v2)

            self.assertTrue(vv.x == v1.x + v2.x)
            self.assertTrue(vv.y == v1.y + v2.y)


    def test_normeVecteur(self):
        # test calcul norme vecteur avec des valeurs positives
        for _ in range(100):
            aleaX = random.randint(0, 1000)
            aleaY = random.randint(0, 1000)
            v = Vecteur.Vecteur(aleaX, aleaY)
            self.assertTrue(v.norme() == math.sqrt(aleaX * aleaX + aleaY * aleaY))

        # test calcul norme vecteur avec des valeurs negatives
        for _ in range(100):
            aleaX = random.randint(-1000, 0)
            aleaY = random.randint(-1000, 0)
            v = Vecteur.Vecteur(aleaX, aleaY)
            self.assertTrue(v.norme() == math.sqrt(aleaX * aleaX + aleaY * aleaY))

        # test calcul norme vecteur avec des valeurs positives et/ou negatives
        for _ in range(100):
            aleaX = random.randint(-500, 500)
            aleaY = random.randint(-500, 500)
            v = Vecteur.Vecteur(aleaX, aleaY)
            self.assertTrue(v.norme() == math.sqrt(aleaX * aleaX + aleaY * aleaY))


    def test_rotation(self):
        rx = random.randint(-50, 50)
        ry = random.randint(-50, 50)

        v = Vecteur.Vecteur(rx, ry)

        angle = random.uniform(-180, 180)

        vx = rx * math.cos(math.radians(angle)) - ry * math.sin(math.radians(angle))
        vy = rx * math.sin(math.radians(angle)) + ry * math.cos(math.radians(angle))

        v = v.rotation(angle)

        self.assertTrue(abs(v.x - vx) < 0.00001)
        self.assertTrue(abs(v.y - vy) < 0.00001)


    def test_symXVecteur(self):
        for _ in range(1000):
            rx = random.randint(-50, 50)
            ry = random.randint(-50, 50)
            v1 = Vecteur.Vecteur(rx, ry)
            v2 = v1.get_sym_x_axis()
            v3 = v1 + v2

            self.assertTrue(v1.norme() == v2.norme())  # test norme vecteur et son symetrique (Ox) sont identiques
            self.assertTrue(v1.x == v2.x)  # test que l'abscisse ne change pas dans le symetrique (Ox)
            self.assertTrue(v3.x == 2 * v1.x)  # test prop. somme vect. et son sym.(Oy) => abscisseX somme est doublé
            self.assertTrue(v3.y == 0)  # test prop. somme vect. et son sym.(Ox) => ordonnéeY somme est nulle


    def test_produitVecteurScalaire(self):
        # tests pour un scalaire entier
        for _ in range(10):
            aleaX = random.randint(-500, 500)
            aleaY = random.randint(-500, 500)
            v = Vecteur.Vecteur(aleaX, aleaY)
            scalaire = random.randint(-500, 500)
            vScalaire = v.__mul__(scalaire)
            vtest = Vecteur.Vecteur(aleaX * scalaire, aleaY * scalaire)
            self.assertTrue(vScalaire.x == vtest.x)
            self.assertTrue(vScalaire.y == vtest.y)
        # tests pour un scalaire flottant
        for _ in range(10):
            aleaX = random.uniform(-500, 500)
            aleaY = random.uniform(-500, 500)
            v = Vecteur.Vecteur(aleaX, aleaY)
            scalaire = random.randint(-500, 500)
            vScalaire = v.__mul__(scalaire)
            vtest = Vecteur.Vecteur(aleaX * scalaire, aleaY * scalaire)
            self.assertTrue(vScalaire.x == vtest.x)
            self.assertTrue(vScalaire.y == vtest.y)

    def test_angle_entre(self):
        """ Vecteur -> Float
        Permet de retourner l'angle entre deux vecteurs (en degrés)
        """
        v = Vecteur.Vecteur(0,1)
        autreVecteur = Vecteur.Vecteur(1, 0)
        self.assertTrue(abs(v.angle_entre(autreVecteur)) - 90. <= 0.00001)

    def test_collision(self):
        """ Tuple(x1,y1) * Vecteur * Tuple(x2,y2) -> Boolean
        Permet de dire s'il y a collision entre deux vecteurs
        """
        v = Vecteur.Vecteur(0,1)
        autreVecteur = Vecteur.Vecteur(1, 0)

        self.assertTrue(v.collision((0.,0.), autreVecteur, (0.,0.)))

        v.y = -1.
        self.assertTrue(v.collision((0.,0.), autreVecteur, (0.,0.)))

        autreVecteur.x = -1
        self.assertTrue(v.collision((0.,0.), autreVecteur, (0.,0.)))
