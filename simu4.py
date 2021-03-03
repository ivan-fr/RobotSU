import models.TerrainContinu
import models.Vecteur
import models.Robot
import models.Polygone

import json

if __name__ == '__main__':
    tc = models.TerrainContinu.Carre(20)
    tc.ajoutPolygone(models.Polygone.hexagone((0, 0), 5))
    tc.robot = models.Robot.Robot(0, 5, 0.8, 0.)
    tc.robot.rotation(90)
    models.TerrainContinu.serialize(tc,"saved.txt")
    Terraindeserialise= models.TerrainContinu.deserialize("saved.txt")
    print(Terraindeserialise)
