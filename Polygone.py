import Vecteur
import math

class Polygone :

    def __init__(self, liste_sommet) :
        self.liste_vecteur = []
        for i in range(len(liste_sommet)-1) :
            x1,y1 = liste_sommet[i]
            x2,y2 = liste_sommet[i+1]
            v = Vecteur.Vecteur(abs(x1-x2),abs(y1-y2))
            self.liste_vecteur.append(v)
        x0,y0 = liste_sommet[0]
        xn,yn = liste_sommet[len(liste_sommet)-1]
        v = Vecteur.Vecteur(abs(x0-xn),abs(y0-yn))
        self.liste_vecteur.append(v)