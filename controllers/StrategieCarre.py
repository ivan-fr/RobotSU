from controllers import StrategieAvancerDroit, StrategieTourner

class StrategieCarre(object):
    def __init__(self, wrapper, robot, vitesse, degreParSeconde, coteCarre):
        self.robot = robot
        self.stratAvancer = StrategieAvancerDroit.StrategieAvancerDroit(coteCarre, vitesse, robot, wrapper)
        self.stratTourner = StrategieTourner.StrategieTourner(90., 20., robot, wrapper)
        self._liste_strategies = []
        self._liste_strategies.append(stratAvancer)
        self._liste_strategies.append(stratTourner)
        
        self.nbCoteParcouru = 0

    def start(self):
        self.nbCoteParcouru = 0
        self._liste_strategies[0].start()
        self._liste_strategies[1].start()

    def step(self):
        if self.stop():
            return

        if not self._liste_strategies[0].stop():
            self._liste_strategies[0].step()
        elif not self._liste_strategies[1].stop():
            self._liste_strategies[1].step()
        
        if self._liste_strategies[1].stop() and self._liste_strategies[0].stop():
            self.nbCoteParcouru += 1

            if self.nbCoteParcouru == 4:
                pass
            else:
                self._liste_strategies[0].start()
                self._liste_strategies[1].start()
    
    def stop(self):
        #condition d'arret lorsque le robot a parcouru les 4 cotes
        return self.nbCoteParcouru == 4
