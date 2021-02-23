import random
from views import Terrain
from models import Robot, Vecteur
import unittest
from math import atan, cos, sin, pi


class TerrainTest(unittest.TestCase):
    def test_AjoutAffichageObjet(self):
        random_ligne = random.randint(11, 100)
        random_colonne = random.randint(11, 100)
        t = Terrain.Terrain(random_ligne, random_colonne)
        random_x = random.randint(1, t.nbLignes - 1)
        random_y = random.randint(1, t.nbColonnes - 1)
        o = object()
        o1 = object()
        cpt = 0
        for _ in range(0, 10):
            while not t.casevide(random_x, random_y):
                random_x = random.randint(1, t.nbLignes)
                random_y = random.randint(1, t.nbColonnes)
            t.ajout_objet(o, random_x, random_y)
            cpt = cpt + 1
        self.assertTrue(
            sum((el is not None for ligne in t.grille for el in ligne)) == cpt)
        self.assertTrue(t.ajout_objet(o, t.nbLignes - 1, t.nbColonnes - 1))
        self.assertTrue(t.ajout_objet(o, 0, 0))
        self.assertTrue(not t.ajout_objet(o, 0, 0))
        self.assertTrue(not t.ajout_objet(o1, -3, 1))
        self.assertTrue(not t.ajout_objet(o1, t.nbLignes, t.nbColonnes))

    def test_dessineVecteur(self):
        t = Terrain.Terrain(1000, 1000, 1)
        v = Vecteur.Vecteur(random.uniform(100., 200),
                            random.uniform(100., 200.))
        posOrigine = (500., 500.)

        t.dessineVecteur(posOrigine, v)

        if v.x == 0. and v.y > 0.:
            angle = pi / 2
        elif v.x == 0. and v.y < 0.:
            angle = - pi / 2
        else:
            angle = atan(v.y / v.x)

        if v.x < 0.:
            angle += pi

        vecteurUnite = Vecteur.Vecteur(
            cos(angle) * t.echelle, sin(angle) * t.echelle)

        traceX = posOrigine[0]
        traceY = posOrigine[1]

        norme = v.norme()

        while Vecteur.Vecteur(traceX - posOrigine[0], traceY - posOrigine[1]).norme() <= norme:
            self.assertFalse(t.ajout_objet_continu(object(), traceX, traceY))
            traceX += vecteurUnite.x
            traceY += vecteurUnite.y

    def test_AjoutContinuObjet(self):
        random_x = random.uniform(11, 100)
        random_y = random.uniform(11, 100)
        t = Terrain.Terrain(100, 100)
        o = object()
        t.ajout_objet_continu(o, random_x, random_y)
        self.assertTrue(
            sum((el is not None for ligne in t.grille for el in ligne)) == 1)
        self.assertTrue(
            t.grille[t.nbLignes - 1 - int(random_y / t.echelle)][int(random_x / t.echelle)] == o)

    def test_Affichage(self):
        random_ligne = random.randint(1, 100)
        random_colonne = random.randint(1, 100)
        t = Terrain.Terrain(random_ligne, random_colonne)
        # t.affichage()
        t1 = Terrain.Terrain(-1, -1)
        # t1.affichage()
        t2 = Terrain.Terrain(0, 10)
        # t2.affichage()

    def isGrille(self, grille):
        lineLength = len(grille[0])
        return all(lineLength == len(line) for line in grille)

    def test_ConstructTerrain(self):
        random_ligne = random.randint(1, 2000)
        random_colonne = random.randint(1, 2000)
        t = Terrain.Terrain(random_ligne, random_colonne)

        self.assertTrue(t.nbLignes == random_ligne)
        self.assertTrue(t.nbColonnes == random_colonne)
        self.assertTrue(self.isGrille(t.grille))

    def test_Grille(self):
        for _ in range(100):
            random_ligne = random.randint(1, 2000)
            random_colonne = random.randint(1, 2000)

            t = Terrain.Terrain(random_ligne, random_colonne)

            grille = t.creerGrille()

            self.assertTrue(random_ligne == len(grille))
            self.assertTrue(
                all(len(line) == random_colonne for line in grille))

        for i in range(-50, 1):
            t = Terrain.Terrain(i, i)
            grille = t.creerGrille()
            self.assertTrue(0 == len(grille))

    def test_AjoutNAlea(self):
        for _ in range(50):
            random_ligne = random.randint(1, 2000)
            random_colonne = random.randint(1, 2000)

            t = Terrain.Terrain(random_ligne, random_colonne)
            t.ajout_alea(random_colonne)
            self.assertTrue(
                sum((el is not None for ligne in t.grille for el in ligne)) == random_colonne)

        t = Terrain.Terrain(1, 1)
        t.ajout_alea(3)
        self.assertTrue(
            sum((el is not None for ligne in t.grille for el in ligne)) == 0)

    def test_estVide(self):
        o = object()
        # Cas de terrain de taille zero => test HORS tableau dans ce cas précis
        T0 = Terrain.Terrain(0, 0)
        self.assertTrue(any([T0.casevide(x, x)
                             for x in range(-1, 2)]) == False)

        # Cas de terrain vide de taille une => test case vide du tableau + cases hors tableau
        T1 = Terrain.Terrain(1, 1)
        self.assertTrue(T1.casevide(0, 0) == True)
        T1.ajout_objet(o, 0, 0)
        self.assertTrue(any([T1.casevide(x, y) for x in range(-1, 2)
                             for y in range(-1, 2)]) == False)

        # Cas de plusieurs terrains de taille aléatoire, strictement positive et contenant un objet
        for _ in range(1001):
            T = Terrain.Terrain(random.randint(1, 50), random.randint(1, 50))
            aleaX = random.randint(0, T.nbLignes - 1)
            aleaY = random.randint(0, T.nbColonnes - 1)
            T.ajout_objet(o, aleaX, aleaY)

            for l in range(0, T.nbLignes):
                for c in range(0, T.nbColonnes):
                    if l == aleaX and c == aleaY:
                        # Test sur l'unique case non vide du tableau
                        self.assertTrue(T.casevide(l, c) == False)
                    else:
                        # Test sur l'ensemble des cases vide du tableau
                        self.assertTrue(T.casevide(l, c) == True)

    def test_supprimerObjet(self):
        o = object()
        # Cas de terrain de taille zero => test HORS tableau dans ce cas précis
        T0 = Terrain.Terrain(0, 0)
        self.assertTrue(any([T0.supprimerObjet(x, x)
                             for x in range(-1, 2)]) == False)

        # Cas de terrain de taille une
        T1 = Terrain.Terrain(1, 1)
        # Test de la fonction sur les cases hors de la grille
        self.assertTrue(any([T1.supprimerObjet(x, y) for x in range(-1, 2)
                             for y in range(-1, 2) if x != y]) == False)
        # test sur la case VIDE du tableau
        self.assertTrue(T1.supprimerObjet(0, 0) == True)
        T1.ajout_objet(o, 0, 0)
        # test sur case pleine du tableau
        self.assertTrue(T1.supprimerObjet(0, 0))
        self.assertTrue(T1.casevide(0, 0))

        # Cas de plusieurs terrains de taille aléatoire, strictement positive et contenant plusieurs objets
        for _ in range(1000):
            T = Terrain.Terrain(random.randint(2, 50), random.randint(2, 50))
            aleaNbr = random.randint(1, T.nbLignes * T.nbColonnes - 1)
            T.ajout_alea(aleaNbr)
            # Test que la fonction retourne bien True lorsqu'appliquée à une case du terrain
            self.assertTrue(all([T.supprimerObjet(x, y) for x in range(
                0, T.nbLignes) for y in range(0, T.nbColonnes)]))
            # Test toutes cases vide aprés passage fonction
            self.assertTrue(all([T.casevide(x, y) for x in range(
                0, T.nbLignes) for y in range(0, T.nbColonnes)]))

    def test_AffichageRobot(self):
        random_ligne = random.randint(0, 20)
        random_colonne = random.randint(0, 20)
        t = Terrain.Terrain(random_ligne, random_colonne)
        random_x = random.randint(1, t.nbLignes - 1)
        random_y = random.randint(1, t.nbColonnes - 1)
        robot = Robot.Robot(0, 10, 10, 0)
        self.assertTrue(t.ajout_objet(robot, random_x, random_y))
        robot = Robot.Robot(0, 10, 10, 0)
        # robot n'est pas affiché car coordonnees hors du terrain
        self.assertTrue(not t.ajout_objet(robot, -10, -10))
        self.assertTrue(not t.ajout_objet(robot, random_ligne, random_colonne))
        # t.affichage()
