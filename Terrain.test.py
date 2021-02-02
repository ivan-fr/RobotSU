import random
import Terrain

def testAjoutAffichageObjet():
    random_ligne = random.randint(1, 100)
    random_colonne = random.randint(1, 100)
    t = Terrain.Terrain(random_ligne, random_colonne)
    random_x = random.randint(1, t.nbLignes-1)
    random_y = random.randint(1, t.nbColonnes-1)
    o = object()
    o1 = object()
    cpt = 0
    if t.nbLignes * t.nbColonnes >= 10:
        for _ in range(0, 10):
            while not t.casevide(random_x, random_y):
                random_x = random.randint(1, t.nbLignes)
                random_y = random.randint(1, t.nbColonnes)
            t.ajout_objet(o, random_x, random_y)
            cpt = cpt+1
        assert cpt == 10
    assert t.ajout_objet(o, t.nbLignes-1, t.nbColonnes-1)
    assert t.ajout_objet(o, 0, 0)
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


if __name__ == '__main__':
    try:
        testAjoutAffichageObjet()
        print("Test: testAjoutObjet a réussi")
    except AssertionError as e:
        print("Test: testAjoutObjet a échoué !!")

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
