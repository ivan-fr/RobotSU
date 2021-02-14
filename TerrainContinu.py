import Robot
from Terrain import *
import Vecteur

class TerrainContinu(object):
    def __init__(self, vecteurSurface):
        self.vecteurSurface = vecteurSurface
        self.listePolygone = []

    def ajoutPolygone(self, polygone):
        """Polygone -> void 
        ajoute un polygone a l'objet"""
        self.listePolygone.append(polygone)
        return

    def affichageDeContinuADiscret(self):
        """void->void
        affiche le terrain de maniere discrete"""
        x = self.vecteurSurface[0].x
        y = self.vecteurSurface[0].y
        for i in self.vecteurSurface:
            if(i.x > x):
                x = i.x
            if(i.y > y):
                y = i.y
        terrain = Terrain(x, y)
        for i in self.listePolygone:
            for j in range(len(i.liste_sommet - 2)):
                vecteur = Vecteur.Vecteur(i.liste_sommet[j][0]-i.liste_sommet[j+1][0], i.liste_sommet[j][1]-i.liste_sommet[j+1][1])
                vecteurCpy = Vecteur.Vecteur(i.list_sommet[j][0], i.list_sommet[j][1])
                while (vecteur.x != vecteurCpy.x) or (vecteur.y != vecteurCpy.y):
                    terrain.ajout_objet(object(),vecteurCpy.x, vecteurCpy.y)
                    if(vecteur.x > vecteurCpy.x):
                        vecteurCpy.x += 1
                    elif(vecteur.x < vecteurCpy.x):
                        vecteurCpy.x - 1
                    if(vecteur.y > vecteurCpy.y):
                        vecteurCpy.y += 1
                    elif(vecteur.y < vecteurCpy.y):
                        vecteurCpy.y - 1
        terrain.affichage()

    def collision((x,y), vecteurDeplacement) :
        """tuple (int * int) * Vecteur -> boolean
        méthode qui verifie la collision du robot avec les objets contenu sur le terrain ainsi qu'avec 
        les vecteurs qui le delimitent
        : param tuple : coordonnees du robot
        : param Vecteur : vecteur de deplacement du robot
        """
        for p in self.listePolygone :
            if (p.collision((x,y),VecteurDeplacement)) :
                return True
        #posX, posY : position du premier vecteur du terrain
        posX = 0
        posY = 0
        for v in self.vecteurSurface :
            #vecteurDeplacement et (x,y) du robot
            if (v.collision((posX,posY),vecteurDeplacement,(x,y))) :
                return True
            #calcul de l'origine des vecteurs suivants
            poX = posX + v.x
            poY = posY + v.y
        return False
