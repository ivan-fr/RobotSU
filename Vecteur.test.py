import random
import Vecteur
import math

def testConstructVecteur():
	random_x=random.randint(-50, 50)
	random_y=random.randint(-50, 50)
	V = Vecteur.Vecteur(random_x,random_y)
	assert V.x == random_x
	assert V.y == random_y
	
def test__add__():
	for _ in range(1000) :
		v1=Vecteur.Vecteur(random.randint(-50, 50),random.randint(-50, 50))
		v2=Vecteur.Vecteur(random.randint(-50, 50),random.randint(-50, 50))
		vv=v1.__add__(v2)
		assert vv.x == v1.x+v2.x
		assert vv.y == v1.y+v2.y

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

