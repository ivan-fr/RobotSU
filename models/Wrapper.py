from models import RobotIRL, Robot

class Wrapper(object):
    def __init__(self, RobotIRL):
        self.RobotIRL = RobotIRL
        self._vitesse = 0
        self.degreParSeconde = 0

    @property
    def vitesse(self):
        return self._vitesse

    @vitesse.setter
    def vitesse(self, vitesse):
        self.RobotIRL.set_motor_dps("MOTOR_LEFT+MOTOR_RIGHT", vitesse)
        self._vitesse = vitesse

    @property
    def degreParSeconde(self):
        return self.degreParSeconde

    @degreParSeconde.setter
    def degreParSeconde(self, motor, angle):
        """passer en parametres pour motor: MOTOR_LEFT ou MOTOR_RIGHT en fonction de vers où tourner
        ainsi que l'angle"""
        if(motor == "MOTOR_LEFT"):
            self.RobotIRL.set_motor_dps(motor, angle)
            self.RobotIRL.set_motor_dps("MOTOR_RIGHT", -angle)
            self._degreParSeconde = angle
        elif(motor == "MOTOR_RIGHT"):
            self.RobotIRL.set_motor_dps(motor, angle)
            self.RobotIRL.set_motor_dps("MOTOR_LEFT", -angle)
            self._degreParSeconde = angle
        