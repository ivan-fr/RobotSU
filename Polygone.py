import Vecteur


class Polygone :

    def __init__(self, liste_sommet) :
        self.liste_vecteur = []
        self.liste_sommet = liste_sommet
        for i in range(len(liste_sommet)-1) :
            x1,y1 = liste_sommet[i]
            x2,y2 = liste_sommet[i+1]
            v = Vecteur.Vecteur((x1-x2),(y1-y2))
            self.liste_vecteur.append(v)
        x0,y0 = liste_sommet[len(liste_sommet)-1]
        xn,yn = liste_sommet[0]
        v = Vecteur.Vecteur((x0-xn),(y0-yn))
        self.liste_vecteur.append(v)

    def collision(self,posRobot,VecteurDeplacement):
        """tuple(int * int) * Polygone * Vecteur -> boolean
        methode qui verifie la collision du robot avec un objet.
        """
        i=0
        while(i<len(self.liste_sommet)):
            if not (self.liste_vecteur[i].collision(self.liste_sommet[i],VecteurDeplacement,posRobot)):
                return False
            i=i+1
        return True


def Carre(origine,norme):
    n=norme/2
    x,y = origine
    liste_sommet = [(x-n,y-n),(x+n,y-n),(x+n,y-n),(x+n,y+n)]
    return Polygone(liste_sommet)

def Triangle(origine, norme):
    n=norme/2
    x,y=origine
    liste_sommet=[(x-n,y),(x+n,y-n),(x+n,y+n)]
    return Polygone(liste_sommet)

def hexagone(origine,norme):
    n=norme/2
    x,y=origine
    liste_sommet=[(x-norme,y),(x-n,y-n),(x+n,y-n),(x+norme,y),(x+n,y+n),(x-n,y+n)]
    return Polygone(liste_sommet)

    
