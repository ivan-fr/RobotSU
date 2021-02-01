class Terrain(object):
    def __init__(self, nbLignes, nbColonnes):
        self.nbLignes = nbLignes
        self.nbColonnes = nbColonnes

    def grille(self):
        """
        Retourne la grille du terrain, cad un tableau de tableau (remplis de None=vide)
        """
        return [[None] * self.nbColonnes] * self.nbLignes

    def casevide(self, x, y, grille):
        """ int * int * tab [][] -> boolean
        retourne vrai si la case est vide, et faux si celle-ci est occupee"""
        if x > self.nbLignes or y > self.nbColonnes:
            print("cette case n'est pas dans le tableau")
            return False
        if grille[x][y] is None:
            return True
        return False