import datetime


class StrategieTournerIRL(object):
    def __init__(self, wrapper, angleTarget, degreParSeconde):
        self.angleTarget = angleTarget
        self.angleApplique = 0.
        self.wrapper = wrapper
        self.degreParSeconde = degreParSeconde
        self.lastUpdate = None

    def start(self):
        self.angleApplique = 0.
        self.lastUpdate = None

    def step(self):
        if self.stop():
            return

        self.wrapper.rotation = self.degreParSeconde

        if self.lastUpdate is None:
            self.lastUpdate = datetime.datetime.now()
        else:
            now = datetime.datetime.now()
            deltaT = (now - self.lastUpdate).total_seconds()
            self.lastUpdate = now
            self.angleApplique += deltaT * abs(self.degreParSeconde)

    def stop(self):
        # condition d'arret, si le robot a bien tourne
        result = self.angleApplique >= self.angleTarget
        if result:
            self.wrapper.rotation = 0.
        return result
