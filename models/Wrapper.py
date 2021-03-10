from models import RobotIRL, Robot

class Wrapper(object):
    def __init__(self, RobotIRL):
        self.RobotIRL = RobotIRL
        self._vitesse = 0
        self._rotation = 0

    @property
    def vitesse(self):
        return self._vitesse

    @vitesse.setter
    def vitesse(self, vitesse):
        self.RobotIRL.set_motor_dps("MOTOR_LEFT+MOTOR_RIGHT", vitesse)
        self._vitesse = vitesse

    @property
    def rotation(self):
        return self._rotation

    @rotation.setter
    def rotation(self, motor, angle):
        """passer en parametres pour motor: MOTOR_LEFT ou MOTOR_RIGHT en fonction de vers où tourner
        ainsi que l'angle"""
        self.RobotIRL.set_motor_dps(motor, angle)
        self._rotation = angle