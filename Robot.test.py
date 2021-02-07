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
