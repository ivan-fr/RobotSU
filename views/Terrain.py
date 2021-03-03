import random
import time
from models import Vecteur, Robot
from math import atan, sin, cos, pi
import platform
import curses


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

    def ajout_objet(self, objet, ligne, colonne):
        """Object * int *int ->boolean
        Place un objet donné en argument dans la case[x][y] du terrain en verifiant s'il est vide."""
        if (self.casevide(ligne, colonne)):
            self.grille[ligne][colonne] = objet
            return True
        return False

    def ajout_objet_continu(self, objet, x, y):
        return self.ajout_objet(
            objet,
            self.nbLignes - 1 - int((y + int(abs(self.yMin))) / self.echelle),
            int((x + int(abs(self.xMin))) / self.echelle) 
        )

    def ajout_alea(self, nbitem):
        """Object * int -> boolean
        Place item nbfois aleatoirement sur le Terrain."""
        if (self.nbLignes * self.nbColonnes > nbitem):
            for _ in range(nbitem):
                o = object()
                a = random.randint(0, self.nbLignes)
                b = random.randint(0, self.nbColonnes)
                while (self.casevide(a, b) == False):
                    a = random.randint(0, self.nbLignes)
                    b = random.randint(0, self.nbColonnes)
                self.ajout_objet(o, a, b)
            return True
        return False

    def affichage(self):
        """affiche le Terrain"""
        bordure = "".join(["+", "-" * self.nbColonnes, "+"])
        print(bordure)
        for i in self.grille:
            print("|", end="")
            for j in i:
                if j is None:
                    print(" ", end="")
                elif isinstance(j, Robot.Robot):
                    print("R", end="")
                else:
                    print("X", end="")
            print("|", end="")
            print()
        print(bordure + "\n")

    def supprimerObjet(self, x, y):
        """int * int -> bool
        met la case à None"""
        if (x < 0 or y < 0 or x >= self.nbLignes or y >= self.nbColonnes):
            return False
        self.grille[x][y] = None
        return True

    def supprimerAffichage(self):
        """void -> void
        supprime l'affichage du terminal"""
        stdscr = curses.initscr()
        time.sleep(1)
        stdscr.clear()
        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        return

    def dessineVecteur(self, posOrigine, vecteur):
        if vecteur.x == 0. and vecteur.y > 0.:
            angle = pi / 2
        elif vecteur.x == 0. and vecteur.y < 0.:
            angle = - pi / 2
        else:
            angle = atan(vecteur.y / vecteur.x)

        if vecteur.x < 0.:
            angle += pi

        vecteurUnite = Vecteur.Vecteur(cos(angle) * self.echelle, sin(angle) * self.echelle)

        traceX = posOrigine[0]
        traceY = posOrigine[1]

        norme = vecteur.norme()

        while Vecteur.Vecteur(traceX - posOrigine[0], traceY - posOrigine[1]).norme() <= norme:
            self.ajout_objet_continu(object(), traceX, traceY)
            traceX += vecteurUnite.x
            traceY += vecteurUnite.y


def construireTerrain(terrainContinu, echelle):
    """return Terrain
    affiche le terrain de maniere discrete
    echelle: combien de case par unité. La valeur de l'unité est dans la variable echelle
    """

    # determine les dimensions idéal du terrain
    xMax = None
    yMax = None
    xMin = None
    yMin = None
    for sommetSurface in terrainContinu.polygoneSurface.liste_sommet:
        x, y = sommetSurface

        if xMax is None or x > xMax:
            xMax = x
        if yMax is None or y > yMax:
            yMax = y

        if xMin is None or x < xMin:
            xMin = x
        if yMin is None or y < yMin:
            yMin = y

    # x 1.1 pour les problèmes d'affichage lié aux approximations
    terrain = Terrain(abs(yMin - yMax) + echelle, abs(xMax - xMin) + echelle, echelle, xMin, yMin)

    if terrainContinu.robot is not None:
        terrain.ajout_objet_continu(terrainContinu.robot, terrainContinu.robot.x, terrainContinu.robot.y)

    # dessine la delimitation
    x = terrainContinu.polygoneSurface.liste_sommet[0][0]
    y = terrainContinu.polygoneSurface.liste_sommet[0][1]
    for sommetSurface in terrainContinu.polygoneSurface.liste_vecteur:
        terrain.dessineVecteur((x, y), sommetSurface)
        x += sommetSurface.x
        y += sommetSurface.y

    # dessine les polygones
    for polygone in terrainContinu.listePolygone:
        for i in range(len(polygone.liste_vecteur)):
            terrain.dessineVecteur(polygone.liste_sommet[i], polygone.liste_vecteur[i])

    return terrain
