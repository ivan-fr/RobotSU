import Terrain
import Vecteur
import Robot
import random
import Polygone
import TerrainContinu

if __name__ == '__main__':
    tc = TerrainContinu.Carre(20, (10, 1))
    tc.ajoutPolygone(Polygone.hexagone((10,10), 5))
    tc.robot.rotation(90)

    while True:
        tc.robot.avance(1)
        t = Terrain.construireTerrain(tc, 0.5)
        t.affichage()

        if not tc.robot.collision(tc):
            t.supprimerAffichage()
        else:
            break
        
    print("Le robot a rencontrer un obstacle !")