from random import *
class Gemme(object):
    def __init__(self, x , y):
        self.x = (int)(random() * x)
        self.y = (int)(random() * y)
        self.dureeVie = (int)(random() * 15)