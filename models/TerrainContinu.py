from models import Robot
from models import Vecteur, Polygone


class TerrainContinu(object):
    def __init__(self, polygoneSurface, robot=None):
        self.polygoneSurface = polygoneSurface
        self.robot = robot
        self.listePolygone = []

    def ajoutPolygone(self, polygone):
        """Polygone -> void 
        ajoute un polygone a l'objet"""
        self.listePolygone.append(polygone)
        return

    def collision(self, posOrigine, vecteurDeplacement):
        """tuple (int * int) * Vecteur -> boolean
        méthode qui verifie la collision du robot avec les objets contenu sur le terrain ainsi qu'avec 
        les vecteurs qui le delimitent
        : param tuple : coordonnees du robot
        : param Vecteur : vecteur de deplacement du robot
        """
        for p in self.listePolygone:
            if p.collision(posOrigine, vecteurDeplacement):
                return True
        # posX, posY : position du premier vecteur du terrain
        posX = self.polygoneSurface.liste_sommet[0][0]
        posY = self.polygoneSurface.liste_sommet[1][1]
        for v in self.polygoneSurface.liste_vecteur:
            # vecteurDeplacement et (x,y) du robot
            if (v.collision((posX, posY), vecteurDeplacement, posOrigine)):
                return True
            # calcul de l'origine des vecteurs suivants
            posX = posX + v.x
            posY = posY + v.y
        return False


def Carre(norme):
    return TerrainContinu(Polygone.Carre((0.,0.), norme))
