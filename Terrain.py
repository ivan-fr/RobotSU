import random 
import Robot
import os
import time
import Vecteur
from math import atan, sin, cos, pi

class Terrain(object):
    def __init__(self, nbLignes, nbColonnes, echelle=1):
        self.echelle = echelle
        self.nbLignes = int(nbLignes / echelle)
        self.nbColonnes = int(nbColonnes / echelle)
        self.grille = self.creerGrille()

    def creerGrille(self):
        """
        -> list[list[NoneType]]
        Retourne la grille du terrain, cad un tableau multidimensionnel vide
        """
        return [[None] * self.nbColonnes for _ in range(self.nbLignes)]
    
    def casevide(self, x, y):
        """ int * int * tab [][] -> boolean
        retourne vrai si la case est vide, et faux si celle-ci est occupee"""
        if x >= self.nbLignes or x < 0 or y >= self.nbColonnes or y < 0:
            return False
        if self.grille[x][y] is None:
            return True
        return False

    def ajout_objet(self,objet,x,y) : 
        """Object * int *int ->boolean
        Place un objet donné en argument dans la case[x][y] du terrain en verifiant s'il est vide."""
        if(self.casevide(x,y)):
            self.grille[x][y]=objet 
            return True
        return False

    def ajout_alea(self,nbitem):
        """Object * int -> boolean
        Place item nbfois aleatoirement sur le Terrain."""
        if (self.nbLignes*self.nbColonnes > nbitem):
            for _ in range(nbitem):
                o=object()
                a=random.randint(0, self.nbLignes)
                b=random.randint(0, self.nbColonnes)
                while(self.casevide(a,b)==False) : 
                    a=random.randint(0, self.nbLignes)
                    b=random.randint(0, self.nbColonnes)
                self.ajout_objet(o,a,b)
            return True
        return False 

    def affichage(self):
        """affiche le Terrain"""
        bordure="".join(["+","-" * self.nbColonnes,"+"])
        print(bordure)
        for i in self.grille:
            print("|",end="")
            for j in i:
                if j is None:
                    print(" ", end="")
                elif isinstance(j, Robot.Robot):
                    print("R", end="")
                else:
                    print("X", end="")
            print("|",end="")
            print()
        print(bordure+"\n")

    def supprimerObjet(self, x, y):
        """int * int -> bool
        met la case à None"""
        if(x < 0 or y < 0 or x >= self.nbLignes or y >= self.nbColonnes):
            return False
        self.grille[x][y] = None
        return True

    def supprimerAffichage(self):
        """void -> void
        supprime l'affichage du terminal"""
        time.sleep(1)
        os.system('cls')
        return

    def dessineVecteur(self, posOrigine, vecteur):
        posTarget = (posOrigine[0] + vecteur.x, posOrigine[1] + vecteur.y)
        angle = atan(vecteur.y / vecteur.x)

        if vecteur.x < 0.:
            angle += pi

        vecteurUnite = Vecteur.Vecteur(cos(angle), sin(angle))

        traceX = posOrigine[0]
        traceY = posOrigine[1]

        while traceX < posTarget[0] and traceY < posTarget[1]:
            self.ajout_objet(
                object(),
                int(traceX / self.echelle),
                self.nbLignes - 1 - int(traceY / self.echelle)
            )

            traceX += vecteurUnite.x
            traceY += vecteurUnite.y


def construireTerrain(terrainContinu, echelle):
    """return Terrain
    affiche le terrain de maniere discrete
    echelle: combien de case par unité. La valeur de l'unité est dans la variable echelle
    """

    # determine les dimensions idéal du terrain
    x = 0.
    y = 0.
    xMax = 0.
    yMax = 0.
    for vecteurSurface in terrainContinu.vecteursSurface:
        targetX = vecteurSurface.x + x
        targetY = vecteurSurface.y + y

        if targetX > xMax:
            xMax = targetX
        if targetY > yMax:
            yMax = targetY

        x = targetX
        y = targetY

    terrain = Terrain(xMax, yMax, echelle)

    # dessine la delimitation
    x = 0.
    y = 0.
    for vecteurSurface in terrainContinu.vecteursSurface:
        terrain.dessineVecteur((x, y), vecteurSurface)
        x += vecteurSurface.x
        y += vecteurSurface.y

    # dessine les polygones
    for polygone in terrainContinu.listePolygone:
        for i in range(len(polygone.liste_vecteur)):
            terrain.dessineVecteur(polygone.liste_sommet[i], polygone.liste_vecteur[i])
