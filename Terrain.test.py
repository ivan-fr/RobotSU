import random
import Terrain



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
        testConstructTerrain()
        print("Test: Constructeur du terrain réussi")
    except AssertionError as e:
        print("Test: Constructeur du terrain a échoué !!")

    try:
        testGrille()
        print("Test: Generation des grilles réussi")
    except AssertionError as e:
        print("Test: Generation des grilles a échoué !!")
