from views import Terrain
from models import Robot
from models import Vecteur
import time
Terrain = Terrain.Terrain(20, 20)
Robot = Robot.Robot(2,2)
Vecteur = Vecteur.Vecteur(2,0)
Robot.vecteurDeplacement = Vecteur

Terrain.affichage()
Terrain.ajout_objet(Robot, Robot.x, Robot.y)
i = 0
while i < 5:
    Robot.avance(1)
    if(i % 2 == 0):
        Terrain.ecrire(Robot)
    else:
        Terrain.ajout_objet(Robot, Robot.x, Robot.y)
    Terrain.affichage()
    time.sleep(1.)
    i+= 1