from views import Terrain
from models import Polygone, TerrainContinu, Robot

if __name__ == '__main__':
    tc = TerrainContinu.Carre(20)
    tc.ajoutPolygone(Polygone.hexagone((0, 0), 5))
    tc.robot = Robot.Robot(0,5, 0.8, 0.)
    tc.robot.rotation(90)

    while not tc.robot.collision(tc, 1):
        tc.robot.avance(1)
        t = Terrain.construireTerrain(tc,1)
        t.affichage()
        if not tc.robot.collision(tc, 1):
            t.supprimerAffichage()
        else:
            break

    print("Le robot a rencontrer un obstacle !")
