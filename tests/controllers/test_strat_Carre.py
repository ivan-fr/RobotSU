import random
from models import Robot
from controllers import StrategieCarre
import math
import unittest

        
class CarreTest(unittest.TestCase):
    def test_contruct_StratCarre(self):
        # pour creation robot
        random_x = random.randint(0, 50)
        random_y = random.randint(0, 50)
        random_vitesse = random.uniform(-50, 50)
        random_angle = random.uniform(-180., 180.)
        r = Robot.Robot(random_x, random_y, random_vitesse, random_angle)
        degrePS = random.randint(0, 20)
        normeCote = random.randint(0, 10)
        stratC = StrategieCarre.StrategieCarre(r,random_vitesse,degrePS,normeCote)

        self.assertTrue(stratC.robot == r)
        self.assertTrue(stratC.nbCoteParcouru == 0)

        self.assertTrue(stratC.stratAvancer.distance == normeCote)
        self.assertTrue(stratC.stratAvancer.vitesse == random_vitesse)
        self.assertTrue(stratC.stratAvancer.robot == stratC.robot)
        
        self.assertTrue(stratC.stratTourner.angleTarget == 90)
        self.assertTrue(stratC.stratTourner.degreParSeconde == 20)
        self.assertTrue(stratC.stratTourner.robot == stratC.robot)

    def test_Carre(self):
        for i in range(3):
            random_x = random.randint(0, 50)
            random_y = random.randint(0, 50)
            random_vitesse = random.uniform(-50, 50)
            random_angle = random.uniform(-180., 180.)
            r = Robot.Robot(random_x, random_y, random_vitesse, random_angle)
            degrePS = random.randint(0, 20)
            normeCote = random.randint(0, 10)
            stratC = StrategieCarre.StrategieCarre(r,random_vitesse,degrePS,normeCote)
            print("test Carre :",i+1," de longueur ",normeCote)

            stratC.start()
            self.assertTrue(stratC.nbCoteParcouru == 0)
            
            self.assertTrue(stratC.stratTourner.angleApplique == 0.)
            self.assertTrue(stratC.stratTourner.robot._degreParSeconde == 0.)
            self.assertIsNone(stratC.stratTourner.lastUpdate)

            self.assertTrue(stratC.stratAvancer.parcouru == 0)
            self.assertTrue(stratC.stratAvancer.robot.vitesse == 0.)
            self.assertIsNone(stratC.stratAvancer.lastUpdate)

            while not stratC.stop():
                stratC.step()
                self.assertTrue(stratC.nbCoteParcouru <= 4)

            self.assertTrue(stratC.nbCoteParcouru == 4)
            print("les quatres cote du carre ont ete fait")
            
            if(stratC.nbCoteParcouru == 4):
                stratC.stop()
                self.assertTrue(stratC.nbCoteParcouru == 4)
            
