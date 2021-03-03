import models.Robot
import models.Vecteur, models.Polygone
import json


class TerrainContinu(object):
    def __init__(self, polygoneSurface, robot=None, listePolygone=[]):
        self.polygoneSurface = polygoneSurface
        self.robot = robot
        self.listePolygone = listePolygone

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
    return TerrainContinu(models.Polygone.Carre((0.,0.), norme))

def my_enc(TerrainContinu):
    dic = {k:v for k,v in TerrainContinu.__dict__.items() if not k.startswith("_")}
    dic.update({"__class": TerrainContinu.__class__.__name__})
    return dic

def my_hook(dic):
    if "__class" in dic:
        cls = dic.pop("__class")
        return eval(f"models.{cls}.{cls}")(**dic)
    return dic

def serialize(TerrainContinu,filename):
    f = open(filename,"w")
    s = json.dumps(TerrainContinu, default=my_enc, indent=4, sort_keys=True)
    json.dump(s,f)
    f.close()
    return 


def deserialize(filename):
    dic = json.load(open(filename,"r"))
    return json.loads(dic, object_hook=my_hook)
