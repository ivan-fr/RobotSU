import random
import time
from models import Vecteur, Robot
from math import atan, sin, cos, pi
import os
import time
import random

class Terrain(object):
    def __init__(self, nbLignes, nbColonnes, echelle=1, xMin=0., yMin=0.):
        self.echelle = echelle
        self.xMin = xMin
        self.yMin = yMin
        self.nbLignes = int(nbLignes / echelle)
        self.nbColonnes = int(nbColonnes / echelle)
        self.grille = self.creerGrille()

     def creerGrille(self):
        """
        -> list[list[NoneType]]
        Retourne la grille du terrain, cad un tableau multidimensionnel vide
        """
        return [[None] * self.nbColonnes for _ in range(self.nbLignes)]

    def casevide(self, ligne, colonne):
        """ int * int * tab [][] -> boolean
        retourne vrai si la case est vide, et faux si celle-ci est occupee"""
        if ligne >= self.nbLignes or ligne < 0 or colonne >= self.nbColonnes or colonne < 0:
            return False
        if self.grille[ligne][colonne] is None:
            return True
        return False

    def generation_gemme(self, objet):
        """Object * int *int ->boolean
        Place un objet qu'on considere comme une gemme donné en argument dans la case[x][y] du terrain en verifiant s'il est vide."""
        if (self.casevide(ligne, colonne)):
            for i in range(20):
                time.sleep(1)
            self.grille[random.randint(self.nbLignes)][random.int(self.nbColonne]) = objet
            return True
        return False

    def disparition_gemme(self):
        
