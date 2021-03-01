import math
from models import Robot

class StrategieAvancerDroit(object) :

    def __init__(self, distance, temps, robot, terrainC):
        self.robot = robot
        self.distance = distance
        self.temps = temps
        self.tc = terrainC

    def start(self):
        self.parcouru = 0
        self.pos_x = self.robot.x
        self.pos_y = self.robot.y

    def step(self):
        self.tc.robot.avance(self.temps)
        self.parcouru += math.sqrt((self.tc.robot.x - self.pos_x)*(self.tc.robot.x - self.pos_x)+(self.tc.robot.y - self.pos_y)*(self.tc.robot.y - self.pos_y))

    def stop(self):
        #condition d'arret, lorsque que le robot a parcourut la distance souhaitee ou qu'il a rencontre un obstacle
        return (self.parcouru < self.distance) and not (self.tc.robot.collision(self.tc, self.temps))