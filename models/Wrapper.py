import RobotIRL, Robot

class Wrapper(object):
    def __init__(self, RobotIRL):
        self.RobotIRL = RobotIRL

    def setterVitesse(self, vitesse):
        self.RobotIRL.set_motor_dps("MOTOR_LEFT+MOTOR_RIGHT", vitesse)

    def rotationRobot(self, motor, angle):
        """passer en parametres pour motor: MOTOR_LEFT ou MOTOR_RIGHT en fonction de vers où tourner
        ainsi que l'angle"""
        self.RobotIRL.set_motor_dps(motor, angle)