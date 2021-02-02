import random
import Terrain

def testAjoutAffichageObjet():
    random_ligne = random.randint(11, 100)
    random_colonne = random.randint(11, 100)
    t = Terrain.Terrain(random_ligne, random_colonne)
    random_x = random.randint(1, t.nbLignes-1)
    random_y = random.randint(1, t.nbColonnes-1)
    o = object()
    o1 = object()
    cpt = 0
    for _ in range(0, 10):
        while not t.casevide(random_x, random_y):
            random_x = random.randint(1, t.nbLignes)
            random_y = random.randint(1, t.nbColonnes)
        t.ajout_objet(o, random_x, random_y)
        cpt = cpt+1
    assert sum((el is not None for ligne in t.grille for el in ligne)) == cpt
    assert t.ajout_objet(o, t.nbLignes-1, t.nbColonnes-1)
    assert t.ajout_objet(o, 0, 0)
    assert not t.ajout_objet(o, 0, 0)
    assert not t.ajout_objet(o1, -3, 1)
    assert not t.ajout_objet(o1, t.nbLignes, t.nbColonnes)
    t.affichage()

def testAffichage():
    random_ligne = random.randint(1, 100)
    random_colonne = random.randint(1, 100)
    t = Terrain.Terrain(random_ligne, random_colonne)
    #t.affichage()
    t1 = Terrain.Terrain(-1, -1)
    #t1.affichage()
    t2 = Terrain.Terrain(0, 10)
    #t2.affichage()

def isGrille(grille):
    lineLength = len(grille[0])
    return all(lineLength == len(line) for line in grille)

def testConstructTerrain():
    random_ligne = random.randint(1, 2000)
    random_colonne = random.randint(1, 2000)
    t = Terrain.Terrain(random_ligne, random_colonne)

    assert t.nbLignes == random_ligne
    assert t.nbColonnes == random_colonne
    assert isGrille(t.grille)

def testGrille():
    for _ in range(100):
        random_ligne = random.randint(1, 2000)
        random_colonne = random.randint(1, 2000)

        t = Terrain.Terrain(random_ligne, random_colonne)

        grille = t.creerGrille()

        assert random_ligne == len(grille)
        assert all(len(line) == random_colonne for line in grille)

    for i in range(-50, 1):
        t = Terrain.Terrain(i,i)
        grille = t.creerGrille()
        assert 0 == len(grille)


def testAjoutNAlea():
    for _ in range(50):
        random_ligne = random.randint(1, 2000)
        random_colonne = random.randint(1, 2000)

        t = Terrain.Terrain(random_ligne, random_colonne)
        t.ajout_alea(random_colonne)
        assert sum((el is not None for ligne in t.grille for el in ligne)) == random_colonne

    t = Terrain.Terrain(1, 1)
    t.ajout_alea(3)
    assert sum((el is not None for ligne in t.grille for el in ligne)) == 0


def testestVide():
    o = object()
    # Cas de terrain de taille zero
    T0 = Terrain.Terrain(0,0)
    assert any([T0.casevide(x,x) for x in range(-1,2)]) == False

    # Cas de terrain de taille une, contenant un objet
    T1Vide = Terrain.Terrain(1,1)
    assert T1Vide.casevide(-1,-1) == False    # test pour une case hors terrain (inf)
    assert T1Vide.casevide(1,1) == False      # test pour une case hors terrain (sup)
    assert T1Vide.casevide(0,0) == True       # test pour une case vide

    # Cas d'un terrain de taille une contenant un objet
    T1NonVide = Terrain.Terrain(1,1)
    T1NonVide.ajout_objet(o,0,0)
    assert any([T1NonVide.casevide(i,i) for i in range(-1,2)]) == False

    ## Cas de terrain de taille strictement positive quelconque, contenant un objet
    TNonVide = Terrain.Terrain(random.randint(1, 50),random.randint(1, 50))
    aleaX = random.randint(0,TNonVide.nbLignes)
    aleaY = random.randint(0,TNonVide.nbColonnes)
    TNonVide.ajout_objet(o,aleaX,aleaY) 

    for l in range(0,TNonVide.nbLignes):
        for c in range(0,TNonVide.nbColonnes):
            if l==aleaX and c==aleaY:
                assert TNonVide.casevide(l,c) == False
            else:
                assert TNonVide.casevide(l,c) == True

if __name__ == '__main__':
    try:
        testAjoutAffichageObjet()
        print("Test: testAjoutAffichageObjet a réussi")
    except AssertionError as e:
        print("Test: testAjoutAffichageObjet a échoué !!")

    try:
        testAffichage()
        print("Test: testAffichage a réussi")
    except AssertionError as e:
        print("Test: testAffichage a échoué !!")

    try:
        testConstructTerrain()
        print("Test: Constructeur du terrain réussi")
    except AssertionError as e:
        print("Test: Constructeur du terrain a échoué !!")

    try:
        testGrille()
        print("Test: Generation des grilles réussi")
    except AssertionError as e:
        print("Test: Generation des grilles a échoué !!")

    try:
        testAjoutNAlea()
        print("Test: Ajout aléatoire réussi")
    except AssertionError as e:
        print("Test: Ajout aléatoire a échoué !!")

    try:
        testestVide()
        print("Test: methode Terrain.casevide(x,y) réussi")
    except AssertionError as e:
        print("Test: methode Terrain.casevide(x,y) a échoué !!")
