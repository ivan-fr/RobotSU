import models.TerrainContinu
import models.Vecteur
import models.Robot
import models.Polygone
import models.Serializer

import json

if __name__ == '__main__':
    tc = models.TerrainContinu.Carre(20)
    tc.ajoutPolygone(models.Polygone.hexagone((0, 0), 5))
    tc_s = models.Serializer.serialize(tc)
    print(tc_s)
