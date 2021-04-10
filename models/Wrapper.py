import math
import time


class Wrapper(object):
    def __init__(self, RobotIRL):
        self.RobotIRL = RobotIRL
        self.rayon_roue = (self.RobotIRL.WHEEL_DIAMETER * 10e-3) / 2.
        self.rayon_robot = (self.RobotIRL.WHEEL_BASE_WIDTH * 10e-3) / 2.
        self.lastRotation = (None, None)
        self._vitesse = 0.

    @property
    def vitesse(self):
        return self._vitesse

    @vitesse.setter
    def vitesse(self, vitesse):
        self._vitesse = vitesse
        self.lastRotation = self.RobotIRL.get_motor_position()
        dps = (vitesse * 180) / (math.pi * self.rayon_roue)
        self.RobotIRL.set_motor_dps(self.RobotIRL.MOTOR_LEFT + self.RobotIRL.MOTOR_RIGHT, dps)

    @property
    def last_avancement(self):
        if self.lastRotation[0] is None:
            return 0.

        now = self.RobotIRL.get_motor_position()

        radiansRelative = (math.radians(
            now[0] - self.lastRotation[0]), math.radians(now[1] - self.lastRotation[1]))
        distance = (self.rayon_roue * radiansRelative[0] + self.rayon_roue * radiansRelative[1]) / 2.
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
        self.RobotIRL.set_motor_dps(self.RobotIRL.MOTOR_RIGHT, dps)
        self.RobotIRL.set_motor_dps(self.RobotIRL.MOTOR_LEFT, -dps)

    def get_distance(self):
        return self.RobotIRL.get_distance()

    def allumage_led(self):
        self.RobotIRL.set_led(self.RobotIRL.LED_LEFT_EYE, 0, 0, 0)

    def get_image(self):
        return self.RobotIRL.get_image()
