import Terrain
import Vecteur
import Robot

def majAffichageRobot(temps):
    print("start tour t:"+str(temps))
    print("x:"+str(r.x)+" y:"+str(r.y)+" vitesse:"+str(r.vitesse)+" angle:"+str(r.angle))
    r.avance(temps)
    vAdapt = Vecteur.Vecteur(r.x, r.y).rotation(-r.angle * 2)
    T.ajout_objet(r,int(vAdapt.y),int(vAdapt.x))
    print("stop tour t:"+str(temps))
    print("x:"+str(r.x)+" y:"+str(r.y)+" vitesse:"+str(r.vitesse)+" angle:"+str(r.angle))

if __name__ == '__main__':
    print("Initialisation Terrain")
    T = Terrain.Terrain(7,7)
    T.affichage()
    print("Initialisation Robot")
    r = Robot.Robot(0,0,1,45.)
    r.x -= T.nbLignes - 1
    vAdapt = Vecteur.Vecteur(r.x, r.y).rotation(-r.angle * 2)
    T.ajout_objet(r,int(vAdapt.y),int(vAdapt.x))
    print("x:"+str(r.x)+" y:"+str(r.y)+" vitesse:"+str(r.vitesse)+" angle:"+str(r.angle))
    for t in range(0,4):
        majAffichageRobot(t)
        T.affichage()
