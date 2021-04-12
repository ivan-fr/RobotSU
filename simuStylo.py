from views import Terrain
from models import Robot
from models import Vecteur
import time
Terrain = Terrain.Terrain(10, 10)
Robot = Robot.Robot(2,2)
Vecteur = Vecteur.Vecteur(2,2)
Robot.vecteurDeplacement = Vecteur

Terrain.affichage()
Terrain.ajout_objet(Robot, Robot.x, Robot.y)
i = 0
while i < 5:
    Robot.avance(1)
    Terrain.ecrire(Robot)
    Terrain.affichage()
    time.sleep(1.)
    i+= 1