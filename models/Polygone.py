from models import Vecteur
from models import Sommet


class Polygone:

    def __init__(self, liste_sommet, liste_vecteur=None):
        if liste_vecteur is None:
            liste_vecteur = []
        self.liste_vecteur = liste_vecteur
        self._liste_sommet = liste_sommet

        self.liste_sommet = []
        for s in liste_sommet:
            self.liste_sommet.append(Sommet.Sommet(s[0], s[1]))

        if not self.liste_vecteur:
            for i in range(len(liste_sommet) - 1):
                x1, y1 = liste_sommet[i]
                x2, y2 = liste_sommet[i + 1]
                v = Vecteur.Vecteur((x2 - x1), (y2 - y1))
                self.liste_vecteur.append(v)
            x0, y0 = liste_sommet[len(liste_sommet) - 1]
            xn, yn = liste_sommet[0]
            v = Vecteur.Vecteur((xn - x0), (yn - y0))
            self.liste_vecteur.append(v)

    def collision(self, posRobot, VecteurDeplacement):
        """tuple(int * int) *  Vecteur -> boolean
        methode qui verifie la collision du robot avec un objet.
        """
        i = 0
        while (i < len(self._liste_sommet)):
            if self.liste_vecteur[i].collision(self._liste_sommet[i], VecteurDeplacement, posRobot):
                return True
            i = i + 1
        return False


def Carre(origine, norme):
    n = norme / 2
    x, y = origine
    liste_sommet = [(x - n, y - n), (x + n, y - n), (x + n, y + n), (x - n, y + n)]
    return Polygone(liste_sommet)


def Triangle(origine, norme):
    n = norme / 2
    x, y = origine
    liste_sommet = [(x - n, y), (x + n, y - n), (x + n, y + n)]
    return Polygone(liste_sommet)


def hexagone(origine, norme):
    n = norme / 2
    x, y = origine
    liste_sommet = [(x - norme, y), (x - n, y - n), (x + n, y - n), (x + norme, y), (x + n, y + n), (x - n, y + n)]
    return Polygone(liste_sommet)
