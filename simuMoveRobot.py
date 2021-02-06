import Terrain
import Vecteur
import Robot


def majAffichageRobot(temps):
    r.avance(temps)
    vAdapt = Vecteur.Vecteur(r.x, r.y - T.nbLignes + 1).get_sym_x_axis()
    T.ajout_objet(r, int(vAdapt.y), int(vAdapt.x))
    print("ligne:"+str(int(vAdapt.y))+" colonne:"+str(int(vAdapt.x)) +
          " vitesse:"+str(r.vitesse)+" angle:"+str(r.angle))


if __name__ == '__main__':
    print("Initialisation Terrain")
    T = Terrain.Terrain(30, 30)
    r = Robot.Robot(14, 14, 1, -90.)
    vAdapt = Vecteur.Vecteur(r.x, r.y - T.nbLignes + 1).get_sym_x_axis()
    T.ajout_objet(r, int(vAdapt.y), int(vAdapt.x))
    for t in range(0, 8):
        print("start tour t:"+str(t))
        majAffichageRobot(t)
        T.affichage()
