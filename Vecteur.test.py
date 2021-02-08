import random
import Vecteur
import math


def testConstructVecteur():
    random_x = random.randint(-50, 50)
    random_y = random.randint(-50, 50)
    V = Vecteur.Vecteur(random_x, random_y)

    assert V.x == random_x
    assert V.y == random_y


def test__add__():
    for _ in range(1000):
        v1 = Vecteur.Vecteur(random.randint(-500, 500), random.randint(-500, 500))
        v2 = Vecteur.Vecteur(random.randint(-500, 500), random.randint(-500, 500))
        vv = v1.__add__(v2)

        assert vv.x == v1.x+v2.x
        assert vv.y == v1.y+v2.y


def testNormeVecteur():
    # test calcul norme vecteur avec des valeurs positives
    for _ in range(100):
        aleaX = random.randint(0, 1000)
        aleaY = random.randint(0, 1000)
        v = Vecteur.Vecteur(aleaX, aleaY)
        assert v.norme() == math.sqrt(aleaX*aleaX+aleaY*aleaY)

    # test calcul norme vecteur avec des valeurs negatives
    for _ in range(100):
        aleaX = random.randint(-1000, 0)
        aleaY = random.randint(-1000, 0)
        v = Vecteur.Vecteur(aleaX, aleaY)
        assert v.norme() == math.sqrt(aleaX*aleaX+aleaY*aleaY)

    # test calcul norme vecteur avec des valeurs positives et/ou negatives
    for _ in range(100):
        aleaX = random.randint(-500, 500)
        aleaY = random.randint(-500, 500)
        v = Vecteur.Vecteur(aleaX, aleaY)
        assert v.norme() == math.sqrt(aleaX * aleaX + aleaY * aleaY)


def testRotation():
    rx = random.randint(-50,50)
    ry = random.randint(-50,50)

    v = Vecteur.Vecteur(rx, ry)

    angle = random.uniform(-180, 180)

    vx = rx * math.cos(math.radians(angle)) - ry * math.sin(math.radians(angle))
    vy = rx * math.sin(math.radians(angle)) + ry * math.cos(math.radians(angle))

    v = v.rotation(angle)

    assert abs(v.x - vx) < 0.00001    
    assert abs(v.y - vy) < 0.00001    

def testSymXVecteur():
    for _ in range(1000):
        rx = random.randint(-50,50)
        ry = random.randint(-50,50)
        v1 = Vecteur.Vecteur(rx, ry)
        v2 = v1.get_sym_x_axis()
        v3 = v1 + v2

        assert v1.norme() == v2.norme() # test norme vecteur et son symetrique (Ox) sont identiques
        assert v1.x == v2.x             # test que l'abscisse ne change pas dans le symetrique (Ox)
        assert v3.x == 2*v1.x           # test prop. somme vect. et son sym.(Oy) => abscisseX somme est doublé
        assert v3.y == 0                # test prop. somme vect. et son sym.(Ox) => ordonnéeY somme est nulle

def testProduitVecteurScalaire():
    #tests pour un scalaire entier
    for _ in range(10):
        aleaX = random.randint(-500, 500)
        aleaY = random.randint(-500, 500)
        v = Vecteur.Vecteur(aleaX, aleaY)
        scalaire = random.randint(-500, 500)
        vScalaire = v.__mul__(scalaire)
        vtest = Vecteur.Vecteur(aleaX*scalaire, aleaY*scalaire)
        assert vScalaire.x == vtest.x
        assert vScalaire.y == vtest.y
    # tests pour un scalaire flottant
    for _ in range(10):
        aleaX = random.uniform(-500, 500)
        aleaY = random.uniform(-500, 500)
        v = Vecteur.Vecteur(aleaX, aleaY)
        scalaire = random.randint(-500, 500)
        vScalaire = v.__mul__(scalaire)
        vtest = Vecteur.Vecteur(aleaX * scalaire, aleaY * scalaire)
        assert vScalaire.x == vtest.x
        assert vScalaire.y == vtest.y

if __name__ == '__main__':
    try:
        testNormeVecteur()
        print("Test: methode norme réussi")
    except AssertionError as e:
        print("Test: methode norme a échoué !!")

    try:
        testConstructVecteur()
        print("Test: Constructeur de Vecteur réussi")
    except AssertionError as e:
        print("Test: Constructeur de terrain a échoué !!")

    try:
        test__add__()
        print("Test: methode Vecteur._add_ réussi")
    except AssertionError as e:
        print("Test: methode Vecteur.__add__ a échoué !!")

    try:
        testRotation()
        print("Test: methode Vecteur.rotation réussi")
    except AssertionError as e:
        print("Test: methode Vecteur.rotation a échoué !!")

    try:
        testSymXVecteur()
        print("Test: methode get_sym_x_axis() a réussi")
    except AssertionError as e:
        print("Test: methode get_sym_x_axis() a échoué !!")

    try:
        testProduitVecteurScalaire()
        print("Test: methode vecteurScalaire réussi")
    except AssertionError as e:
        print("Test: methode vecteurScalaire a échoué !!")
