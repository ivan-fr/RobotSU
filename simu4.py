import models.TerrainContinu
import models.Vecteur
import models.Robot
import models.Polygone
import models.Serializer

import json

if __name__ == '__main__':
    tc = models.TerrainContinu.Carre(20)
    tc.ajoutPolygone(models.Polygone.hexagone((0, 0), 5))
    robot = models.Robot.Robot(0, 0)
    models.Serializer.serialize(tc, robot)
    terraindeserialise = models.Serializer.deserialize("TC.json")
    robotdeserialise = models.Serializer.deserialize("Robot.json")

    print(terraindeserialise, robotdeserialise)
