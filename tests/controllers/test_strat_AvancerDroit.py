import random
from models import Robot
from controllers import StrategieAvancerDroit
import math
import unittest

# verifier deplacement robot avec coordonnees ?

class AvancerDTest(unittest.TestCase):
    def test_contruct_StratAD(self):
        # pour creation robot
        random_x = random.randint(0, 50)
        random_y = random.randint(0, 50)
        random_vitesse = random.uniform(-50, 50)
        random_angle = random.uniform(-180., 180.)
        r = Robot.Robot(random_x, random_y, random_vitesse, random_angle)
        random_distance = random.uniform(-20, 20)
        stratAD = StrategieAvancerDroit.StrategieAvancerDroit(random_distance,random_vitesse,r)

        self.assertTrue(stratAD.robot == r)
        self.assertTrue(stratAD.distance == random_distance)
        self.assertTrue(stratAD.vitesse == random_vitesse)
        self.assertIsNone(stratAD.lastUpdate)

    def test_Avancer(self):
        for i in range(3):
            random_x = random.randint(0, 50)
            random_y = random.randint(0, 50)
            # si vitesse negative, distance parcourue negative -> ne marche pas
            random_vitesse = random.uniform(0, 50)
            random_angle = random.uniform(-180., 180.)
            r = Robot.Robot(random_x, random_y, random_vitesse, random_angle)
            random_distance = random.uniform(0, 20)
            stratAD = StrategieAvancerDroit.StrategieAvancerDroit(random_distance,random_vitesse,r)
            print("test AD :",i+1," pour une distance de ",stratAD.distance)

            stratAD.start()
            self.assertTrue(stratAD.parcouruSimu == 0)
            self.assertTrue(stratAD.robot.vitesse == 0.)
            self.assertIsNone(stratAD.lastUpdate)

            while not stratAD.stop():
                stratAD.step()
                # 10*0.1 : pour approximation
                self.assertTrue(stratAD.parcouruSimu <= stratAD.distance + 10*0.1)
                # print(stratAD.parcouru , stratAD.distance + 10*0.1)
                self.assertTrue(stratAD.robot.vitesse == stratAD.vitesse)

            self.assertTrue(stratAD.parcouruSimu >= stratAD.distance)

            if(stratAD.parcouruSimu >= stratAD.distance):
                stratAD.stop()
                self.assertTrue(stratAD.robot.vitesse == 0)