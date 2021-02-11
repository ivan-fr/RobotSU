import Vecteur

class Polygone :

    def __init__(self, liste_sommet) :
        self.liste_vecteur = []
        for i in liste_sommet :
            x,y = i
            v = Vecteur.Vecteur(x,y)
            self.liste_vecteur.append(v)