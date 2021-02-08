import random
import Robot
import math

def testConstructRobot():
	random_x=random.randint(0, 50)
	random_y=random.randint(0, 50)
	random_vitesse = random.uniform(0, 10)
	random_angle = random.uniform(-math.pi,math.pi)
	r = Robot.Robot(random_x,random_y,random_vitesse,random_angle)
	
	assert r.x == random_x
	assert r.y == random_y
	assert r.vitesse == random_vitesse
	assert r.angle == random_angle 

def testRotation():
	r = Robot.Robot(0., 0., 1., 0.)
	oldAngle = r.angle
	oldVecteurD = r.vecteurDeplacement
	randomAngleRelative = random.uniform(-180, 180)
	r.rotation(randomAngleRelative)

	oldAngle += randomAngleRelative
	oldAngle %= 360

	if oldAngle > 180.:
		oldAngle -= 360

	assert abs(oldAngle - r.angle) < 0.0001
	
	compare_vecteur = r.vecteurDeplacement + oldVecteurD.rotation(randomAngleRelative) * (-1)
	assert abs(compare_vecteur.norme()) < 0.00001

def test_avance():
    # cas particuliers d'immobilité
    temps = random.randint(1,100)
    pos_x_init = random.uniform(-50, 50)
    pos_y_init = random.uniform(-50, 50)
    vitesse = random.uniform(-10, 10)
    angle =  random.uniform(-180, 180)
    # cas d'une vitesse nulle => immobile
    r = Robot.Robot(pos_x_init, pos_y_init, 0., angle)
    r.avance(temps)
    assert r.x == pos_x_init
    assert r.y == pos_y_init
    # cas d'un temps null => immobile
    r = Robot.Robot(pos_x_init, pos_y_init, vitesse, angle)
    r.avance(0)
    assert r.x == pos_x_init
    assert r.y == pos_y_init

    # cas général, en prenant en compte l'incertitude de calcul --> float (arrondis au 1e-10 pres)
    for _ in range(1000):
        temps = random.randint(1,100)
        pos_x_init = random.uniform(-50, 50)
        pos_y_init = random.uniform(-50, 50)
        vitesse = random.uniform(-10, 10)
        angle =  random.uniform(-180, 180)
        r = Robot.Robot(pos_x_init, pos_y_init, vitesse, angle)
        r.avance(temps)
        pos_x_fin = pos_x_init + ((math.cos(math.radians(angle)) * vitesse) * temps)
        pos_y_fin = pos_y_init + ((math.sin(math.radians(angle)) * vitesse) * temps)
        # ordre de grandeur de l'incertitude = 0,0000000001 prés
        ordre_grandeur = 10**-10
        assert abs(r.x - pos_x_fin) < ordre_grandeur # test que valeurs identiques a 1e-10 prés 
        assert abs(r.y - pos_y_fin) < ordre_grandeur # test que valeurs identiques a 1e-10 prés

	
if __name__ == '__main__':
	try:
		testConstructRobot()
		print("Test: Constructeur de Robot réussi")
	except AssertionError as e:
		print("Test: Constructeur de Robot a échoué !!")

	try:
		testRotation()
		print("Test: rotation de Robot réussi")
	except AssertionError as e:
		print("Test: rotation de Robot a échoué !!")

	try:
		test_avance()
		print("Test: Deplacement du Robot réussi")
	except AssertionError as e:
		print("Test: Deplacement du Robot a échoué !!")
