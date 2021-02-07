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
