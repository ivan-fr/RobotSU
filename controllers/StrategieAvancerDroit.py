import math
from models import Robot

class StrategieAvancerDroit(object) :

    def __init__(self, distance, temps, terrainC):
        self.distance = distance
        self.temps = temps
        self.tc = terrainC

        self.parcouru = 0
        self.pos_x = 0
        self.pos_y = 0

    def start(self):
        self.parcouru = 0
        self.pos_x = self.tc.robot.x
        self.pos_y = self.tc.robot.y

    def step(self):
        self.tc.robot.avance(self.temps)
        self.parcouru += math.sqrt((self.tc.robot.x - self.pos_x) ** 2+(self.tc.robot.y - self.pos_y) ** 2)

    def stop(self):
        #condition d'arret, lorsque que le robot a parcourut la distance souhaitee ou qu'il a rencontre un obstacle
        return (self.parcouru >= self.distance) or (self.tc.robot.collision(self.tc, self.temps))
