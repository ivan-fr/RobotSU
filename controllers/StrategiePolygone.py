import math

class StrategiePolygone(object):
    def __init__(self, stratAvancer, stratTourner, n):
        # 120 degrés pour tourner
        target = math.degrees((n - 2) * math.pi / n)
        dps = target * 0.3
        stratTourner.angleTarget = target
        stratTourner.degreParSeconde = dps

        self.liste_strategies = [stratAvancer, stratTourner] * n
        self.i_liste_strategies = 0

    def start(self):
        self.i_liste_strategies = 0
        self.liste_strategies[self.i_liste_strategies].start()

    def step(self):
        if self.stop():
            return

        if not self.liste_strategies[self.i_liste_strategies].stop():
            self.liste_strategies[self.i_liste_strategies].step()
        else:
            self.i_liste_strategies += 1
            if self.stop():
                return
            else:
                self.liste_strategies[self.i_liste_strategies].start()

    def stop(self):
        #condition d'arret lorsque le robot a parcouru les 4 cotes
        try:
            _ = self.liste_strategies[self.i_liste_strategies]
            return False
        except IndexError:
            return True
