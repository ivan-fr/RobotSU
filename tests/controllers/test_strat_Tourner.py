import random
from models import Robot
from controllers import StrategieTourner
import math
import unittest


class TournerTest(unittest.TestCase):
    def test_contruct_StratT(self):
        # pour creation robot
        random_x = random.randint(0, 50)
        random_y = random.randint(0, 50)
        random_vitesse = random.uniform(-50, 50)
        random_angle = random.uniform(-180., 180.)
        r = Robot.Robot(random_x, random_y, random_vitesse, random_angle)
        degrePS = random.randint(0, 20)
        stratT = StrategieTourner.StrategieTourner(random_angle,degrePS,r)

        self.assertTrue(stratT.robot == r)
        self.assertTrue(stratT.angleTarget == random_angle)
        self.assertTrue(stratT.degreParSeconde == degrePS)
        self.assertTrue(stratT.angleApplique == 0.)
        self.assertIsNone(stratT.lastUpdate)


    def test_rotation(self):
        for i in range(3):
            random_x = random.randint(0, 50)
            random_y = random.randint(0, 50)
            random_vitesse = random.uniform(-50, 50)
            # --> On donne a la strategie seulement des angles positifs ?
            random_angle = random.uniform(0., 20.)
            # random_angle = random.uniform(0., 180.)
            # random_angle = random.uniform(0., 360.)
            # random_angle = random.uniform(-180., 180.)
            r = Robot.Robot(random_x, random_y, random_vitesse, random_angle)
            degrePS = random.randint(1,20)
            stratT = StrategieTourner.StrategieTourner(random_angle,degrePS,r)
            print("test Tourner :",i+1," pour un angle de ",stratT.angleTarget)

            stratT.start()
            self.assertTrue(stratT.angleApplique == 0.)
            self.assertTrue(stratT.robot._degreParSeconde == 0.)
            self.assertIsNone(stratT.lastUpdate)

            while not stratT.stop():
                stratT.step()
                # 10*0.1 : pour approximation
                self.assertTrue(stratT.angleApplique <= stratT.angleTarget + 10*0.1)
                # print(stratT.angleApplique , stratT.angleTarget + 10*0.1)
                self.assertTrue(stratT.robot._degreParSeconde == degrePS)

            self.assertTrue(stratT.angleApplique >= stratT.angleTarget)

            if(stratT.angleApplique >= stratT.angleTarget):
                stratT.stop()
                self.assertTrue(stratT.robot._degreParSeconde == 0.)