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
    
def Carre(origine,norme):
    n=norme/2
    x,y = origine
    liste_sommet = [(x-n,y-n),(x+n,y-n),(x+n,y-n),(x+n,y+n)]
    return Polygone(liste_sommet)

if __name__ == '__main__':
    a=Carre((1,1),1)
    for i in a.liste_vecteur:
        print(i)