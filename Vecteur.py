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
            raise ValueError("Operande n'est pas une instance de la classe Vecteur")
        else:
            return Vecteur(self.x + autreVecteur.x, self.y + autreVecteur.y)




