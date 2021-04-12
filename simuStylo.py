from views import Terrain
from models import Robot
from models import Vecteur

Terrain = Terrain.Terrain(10, 10)
Robot = Robot.Robot(2,2)
Vecteur = Vecteur.Vecteur(2,2)
Robot.vecteurDeplacement = Vecteur

Terrain.affichage()
Terrain.ajout_objet(Robot, Robot.x, Robot.y)
Terrain.ecrire(Robot)
