import math
import time


class Wrapper(object):
    def __init__(self, RobotIRL):
        self.RobotIRL = RobotIRL
        self.rayon_roue = self.RobotIRL.WHEEL_DIAMETER / 2.
        self.lastRotation = (None, None)

    @property
    def vitesse(self):
        return self._vitesse

    @vitesse.setter
    def vitesse(self, vitesse):
        self._vitesse = vitesse
        self.lastRotation = self.RobotIRL.get_motor_position()
        dps = (vitesse * 2 * math.pi) / (360 * self.rayon_roue)
        self.RobotIRL.set_motor_dps(
            self.RobotIRL.MOTOR_LEFT + self.RobotIRL.MOTOR_RIGHT, dps)

    @property
    def last_avancement(self):
        if self.lastRotation[0] is None:
            return 0.

        now = self.RobotIRL.get_motor_position()

        radiansRelative = (math.radians(
            now[0] - self.lastRotation[0]), math.radians(now[1] - self.lastRotation[1]))
        distance = (
            self.rayon_roue * radiansRelative[0] + self.rayon_roue * radiansRelative[1]) / 2.
        return distance

    @property
    def rotation(self):
        return self._rotation

    @rotation.setter
    def rotation(self, dps):
        self._rotation = dps
        self.RobotIRL.set_motor_dps(self.RobotIRL.MOTOR_RIGHT, dps)
        self.RobotIRL.set_motor_dps(self.RobotIRL.MOTOR_LEFT, -dps)

    def get_distance(self):
        return self.RobotIRL.get_distance()

    def allumage_led(self):
        self.RobotIRL.set_led(self.RobotIRL.LED_LEFT_EYE, 0, 0, 0)
