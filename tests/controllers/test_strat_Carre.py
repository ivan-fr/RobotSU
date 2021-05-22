import random
from models import Robot
from controllers import StrategiePolygone, StrategieAvancerDroit, StrategieTourner
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
        normeCote = random.randint(1, 10)
        stratAvancer = StrategieAvancerDroit.StrategieAvancerDroit(r, random_vitesse, normeCote)
        stratTourner = StrategieTourner.StrategieTourner(r, 0., degrePS)
        _ = StrategiePolygone.StrategiePolygone(stratAvancer, stratTourner, 4)

        self.assertTrue(stratTourner.angleTarget == 90.)

    def test_Carre(self):
        for i in range(3):
            random_x = random.randint(0, 50)
            random_y = random.randint(0, 50)
            random_vitesse = random.uniform(-50, 50)
            random_angle = random.uniform(-180., 180.)
            r = Robot.Robot(random_x, random_y, random_vitesse, random_angle)
            degrePS = random.randint(0, 20)
            normeCote = random.randint(1, 10)
            stratAvancer = StrategieAvancerDroit.StrategieAvancerDroit(r, 7., 15.)
            stratTourner = StrategieTourner.StrategieTourner(r, 0., degrePS)
            stratC = StrategiePolygone.StrategiePolygone(stratAvancer, stratTourner, normeCote)

            stratC.start()

            self.assertTrue(stratTourner.angleApplique == 0.)
            self.assertTrue(stratTourner.robot._degreParSeconde == 0.)
            self.assertIsNone(stratTourner.lastUpdate)

            self.assertTrue(stratAvancer.parcouruSimu == 0)
            self.assertTrue(stratAvancer.robot.vitesse == 0.)
            self.assertIsNone(stratAvancer.lastUpdate)

            while not stratC.stop():
                stratC.step()
                self.assertTrue(stratC.i_liste_strategies <= normeCote * 2)

            stratC.stop()
