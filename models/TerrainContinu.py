import models.Vecteur, models.Polygone
import json
import random
import datetime

class TerrainContinu(object):
    def __init__(self, polygoneSurface, listePolygone=[], lastUpdate=None, caseParUnite=0.5):
        self.polygoneSurface = polygoneSurface
        self.listePolygone = listePolygone
        self.lastUpdate = lastUpdate
        self.caseParUnite = caseParUnite
        self.gemmes = []

    def ajout_gemme(self):
        min_x = min(x for x, _ in self.polygoneSurface.liste_sommet)
        max_x = max(x for x, _ in self.polygoneSurface.liste_sommet)

        min_y = min(y for _, y in self.polygoneSurface.liste_sommet)
        max_y = max(y for _, y in self.polygoneSurface.liste_sommet)

        xg = random.uniform(min_x, max_x)
        yg = random.uniform(min_y, max_y)
        self.gemmes.append((xg, yg, datetime.datetime.now(), random.uniform(10, 15)))

    def gemmes_destroy(self):
        to_destroy = []
        for i in range(len(self.gemmes)):
            gemme = self.gemmes[i]
            if (datetime.datetime.now() - gemme[2]).total_seconds() > gemme[3]:
                to_destroy.append(i)
        
        for i in to_destroy:
            self.gemmes.pop(i)

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
        for polygone in self.listePolygone:
            if polygone.collision(posOrigine, vecteurDeplacement):
                return True
        # posX, posY : position du premier vecteur du terrain
        posX = self.polygoneSurface.liste_sommet[0][0]
        posY = self.polygoneSurface.liste_sommet[1][1]
        for vecteur in self.polygoneSurface._liste_vecteur:
            # vecteurDeplacement et (x,y) du robot
            if vecteur.collision((posX, posY), vecteurDeplacement, posOrigine):
                return True
            # calcul de l'origine des vecteurs suivants
            posX = posX + vecteur.x
            posY = posY + vecteur.y
        return False

def Carre(norme):
    return TerrainContinu(models.Polygone.Carre((0.,0.), norme))

def my_enc(obj):
    dic = {k:v for k,v in obj.__dict__.items() if not k.startswith("_")}
    dic.update({"__class": obj.__class__.__name__})
    return dic

def my_hook(dic):
    if "__class" in dic:
        cls = dic.pop("__class")
        return eval(f"models.{cls}.{cls}")(**dic)
    return dic

def serialize(TerrainContinu,filename):
    f = open(filename,"w")
    json.dump(TerrainContinu, f, default=my_enc, indent=4, sort_keys=True)
    f.close()
    return 

def deserialize(filename):
    return json.load(open(filename,"r"), object_hook=my_hook)
