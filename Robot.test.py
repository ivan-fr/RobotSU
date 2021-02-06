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
	
if __name__ == '__main__':
	try:
		testConstructRobot()
		print("Test: Constructeur de Robot réussi")
	except AssertionError as e:
		print("Test: Constructeur de Robot a échoué !!")
