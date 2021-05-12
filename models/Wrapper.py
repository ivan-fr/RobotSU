import math
import time


class Wrapper(object):
    def __init__(self, RobotIRL):
        self.robotIRL = RobotIRL
        self.rayon_roue = (self.robotIRL.WHEEL_DIAMETER * 10e-1) / 2.
        self.rayon_robot = (self.robotIRL.WHEEL_BASE_WIDTH * 10e-1) / 2.
        self.lastRotation = (None, None)
        self._vitesse = 0.

    @property
    def vitesse(self):
        return self._vitesse

    @vitesse.setter
    def vitesse(self, vitesse):
        self._vitesse = vitesse
        self.lastRotation = self.robotIRL.get_motor_position()
        dps = (vitesse * 180) / (math.pi * self.rayon_roue)
        self.robotIRL.set_motor_dps(self.robotIRL.MOTOR_LEFT + self.robotIRL.MOTOR_RIGHT, dps)

    @property
    def last_avancement(self):
        if self.lastRotation[0] is None:
            return 0.

        now = self.robotIRL.get_motor_position()

        radiansRelative = (math.radians(
            now[0] - self.lastRotation[0]), math.radians(now[1] - self.lastRotation[1]))
        distance = (self.rayon_roue * radiansRelative[0] + self.rayon_roue * radiansRelative[1]) / 2.
    
        self.lastRotation = now
        return distance

    @property
    def rotation(self):
        return self._rotation

    @rotation.setter
    def rotation(self, degreParSecondeVoulu):
        self._rotation = degreParSecondeVoulu
        radiansParSecondeVoulu = (degreParSecondeVoulu * math.pi) / 180.
        radiansParSeconde = radiansParSecondeVoulu * self.rayon_robot / self.rayon_roue
        dps = radiansParSeconde * 180. / math.pi
        self.robotIRL.set_motor_dps(self.robotIRL.MOTOR_RIGHT, dps)
        self.robotIRL.set_motor_dps(self.robotIRL.MOTOR_LEFT, -dps)

    def get_distance(self):
        return self.robotIRL.get_distance()

    def allumage_led(self):
        self.robotIRL.set_led(self.robotIRL.LED_LEFT_EYE, 0, 0, 0)

    def get_image(self):
        return self.robotIRL.get_image()
