import Robot
import Terrain
import Vecteur

class TerrainContinu(object):
    def __init__(self):
        self.listePolygone = []

    def ajoutPolygone(self, polygone):
        """Polygone -> void 
        ajoute un polygone a l'objet"""
        self.listePolygone.append(polygone)
        return