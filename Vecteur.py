from math import sqrt

class Vecteur(object):
    """
    Vecteur du plan : 2 dimensions
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """
        -> str
        Permet de retourner une chaine de caractère
        """
        return "("+str(self.x)+","+str(self.y)+")"

    def norme(self):
        """
        -> float
        Retourne la norme du vecteur
        """
        return sqrt(self.x ** 2 + self.y ** 2)
