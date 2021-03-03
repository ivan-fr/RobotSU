import math
from models import Robot

class StrategieAvancerDroit(object) :
    def __init__(self, distance, vitesse, terrainC):
        self.distance = distance
        self.vitesse = vitesse
        self.tc = terrainC

        self.parcouru = 0
        self.pos_x = 0
        self.pos_y = 0

    def start(self):
        self.parcouru = 0
        self.pos_x = self.tc.robot.x
        self.pos_y = self.tc.robot.y
        self.tc.robot.vitesse = self.vitesse

    def step(self):
        self.parcouru += math.sqrt((self.tc.robot.x - self.pos_x) ** 2+(self.tc.robot.y - self.pos_y) ** 2)

    def stop(self):
        #condition d'arret, lorsque que le robot a parcourut la distance souhaitee ou qu'il a rencontre un obstacle
        result = self.parcouru >= self.distance
        if result:
            self.tc.robot.vitesse = 0
        return result
