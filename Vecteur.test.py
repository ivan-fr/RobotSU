import random
import Vecteur
import math

def testNormeVecteur():
    #test calcul norme vecteur avec des valeurs positives
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

if __name__ == '__main__':
    try:
        testNormeVecteur()
        print("Test: methode norme réussi")
    except AssertionError as e:
        print("Test: methode norme a échoué !!")