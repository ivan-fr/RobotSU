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
        self.step()

    def step(self):
        if self.stop() : return
        self.robot.avance(self.temps)
        self.parcouru += math.sqrt((self.robot.x - self.pos_x)*(self.robot.x - self.pos_x)+(self.robot.y - self.pos_y)*(self.robot.y - self.pos_y))
        print(self.distance, self.parcouru)

    def stop(self):
        return (self.parcouru >= self.distance) and (not self.robot.collision(self.tc, self.temps))