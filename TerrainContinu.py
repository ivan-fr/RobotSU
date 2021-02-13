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

        
