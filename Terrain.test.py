import random
import Terrain

def testGrille():
    for _ in range(100):
        random_ligne = random.randint(1, 2000)
        random_colonne = random.randint(1, 2000)

        t = Terrain.Terrain(random_ligne, random_colonne)

        grille = t.grille()

        assert random_ligne == len(grille)
        assert all(len(line) == random_colonne for line in grille)

    for i in range(-50, 1):
        t = Terrain.Terrain(i,i)
        grille = t.grille()
        assert 0 == len(grille)


if __name__ == '__main__':
    try:
        testGrille()
        print("Test: Create Grille successful")
    except AssertionError as e:
        print(e)
