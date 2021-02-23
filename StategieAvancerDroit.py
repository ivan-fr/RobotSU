import math
from models import Robot

class StategieAvancerDroit :

    def __init__(self, distance, temps, robot):
        self.robot = robot
        self.pos_init_x = self.robot.x
        self.pos_init_y = self.robot.y
        self.pos_x = self.robot.x
        self.pos_y = self.robot.y
        self.distance = distance
        self.temps = temps

    def start(self):
        self.parcouru = 0

    def step(self):
        self.parcouru += math.sqrt((self.robot.x - self.pos_x)*(self.robot.x - self.pos_x)+(self.robot.y - self.pos_y)*(self.robot.y - self.pos_y))
        if self.stop() : return 
        self.avancer(self.temps)

    def stop(self):
        return self.parcouru > self.distance