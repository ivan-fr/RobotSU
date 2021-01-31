class Terrain(object):
    def __init__(self, nbLignes, nbColonnes):
        self.nbLignes = nbLignes
        self.nbColonnes = nbColonnes

    def grille(self):
        """
        Retourne la grille du terrain, cad un tableau de tableau (remplis de None=vide)
        """
        return [[None] * self.nbColonnes] * self.nbLignes
