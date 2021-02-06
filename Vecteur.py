from math import sqrt, cos, sin

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
        Permet de retourner une chaine de caractère représentant le vecteur
        """
        return "("+str(self.x)+","+str(self.y)+")"

    def norme(self):
        """
        -> float
        Retourne la norme du vecteur
        """
        return sqrt(self.x ** 2 + self.y ** 2)

    def __add__(self, autreVecteur):
        """
        Vecteur -> Vecteur
        Retourne un vecteur résultant de la somme du vecteur instance avec un autre vecteur
        """
        if not isinstance(autreVecteur, Vecteur):
            raise ValueError("L'Operande n'est pas une instance de la classe Vecteur")
        else:
            return Vecteur(self.x + autreVecteur.x, self.y + autreVecteur.y)

    def __mul__(self, scal):
        """
        Number -> Vecteur
        Retourne un vecteur résultant du produit du vecteur instance avec un scalaire
        """
        if isinstance(scal, int) or isinstance(scal, float):
            return Vecteur(self.x * scal, self.y * scal)
        else:
            raise ValueError("L'Operande n'est pas un scalaire")

    def rotation(self, angle):
        """retourne le vecteur deplacement"""
        if not isinstance(angle, float) or not isinstance(angle, int):
            raise ValueError("L'Operande n'est pas un angle")

        vx = self.x * cos(angle) - self.y * sin(angle)
        vy = self.x * sin(angle) + self.y * cos(angle)

        return Vecteur(vx, vy)
