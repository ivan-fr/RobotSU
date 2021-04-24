import models.Vecteur
import models.Polygone
import datetime


class TerrainContinu(object):
    def __init__(self, polygoneSurface, listePolygone=[], lastUpdate=None, caseParUnite=0.5):
        self.polygoneSurface = polygoneSurface
        self.listePolygone = listePolygone
        self.caseParUnite = caseParUnite

    def ajoutPolygone(self, polygone):
        """Polygone -> void 
        ajoute un polygone a l'objet"""
        self.listePolygone.append(polygone)

    def collision(self, posOrigine, vecteurDeplacement):
        """tuple (int * int) * Vecteur -> boolean
        méthode qui verifie la collision du robot avec les objets contenu sur le terrain ainsi qu'avec 
        les vecteurs qui le delimitent
        : param tuple : coordonnees du robot
        : param Vecteur : vecteur de deplacement du robot
        """
        for polygone in self.listePolygone:
            if polygone.collision(posOrigine, vecteurDeplacement):
                return True
        # posX, posY : position du premier vecteur du terrain
        posX = self.polygoneSurface.liste_sommet[0][0]
        posY = self.polygoneSurface.liste_sommet[1][1]
        for vecteur in self.polygoneSurface.liste_vecteur:
            # vecteurDeplacement et (x,y) du robot
            if vecteur.collision((posX, posY), vecteurDeplacement, posOrigine):
                return True
            # calcul de l'origine des vecteurs suivants
            posX = posX + vecteur.x
            posY = posY + vecteur.y
        return False


def Carre(norme):
    return TerrainContinu(models.Polygone.Carre((0., 0.), norme))
