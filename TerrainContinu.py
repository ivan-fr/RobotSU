import Robot
import Terrain
import Vecteur

class TerrainContinu(object):
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
        self.listePolygone = []

    def ajoutPolygone(self, polygone):
        """Polygone -> void 
        ajoute un polygone a l'objet"""
        self.listePolygone.append(polygone)
        return