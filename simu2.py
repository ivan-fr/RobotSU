import Terrain
import Vecteur
import Robot
import random


def majAffichageRobot(r, t):
    r.avance(1)
    vAdapt = Vecteur.Vecteur(r.x, r.y - t.nbLignes + 1).get_sym_x_axis()
    t.ajout_objet(r, int(vAdapt.y), int(vAdapt.x))


if __name__ == '__main__':
    t = Terrain.Terrain(30, 80)
    r = Robot.Robot(40, 15, 1, 0.)
    for i in range(40):
        majAffichageRobot(r, t)
        r.rotation(random.uniform(-15., 15.))
    
    t.affichage()

    t2 = Terrain.Terrain(30, 80)
    r2 = Robot.Robot(40, 15, 1, 0.)
    for i in range(36):
        majAffichageRobot(r2, t2)
        r2.rotation(10)
    
    t2.affichage()
