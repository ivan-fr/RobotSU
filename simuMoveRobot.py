import Terrain
import Robot

def majAffichageRobot(temps):
    print("start tour t:"+str(temps))
    print("x:"+str(r.x)+" y:"+str(r.y)+" vitesse:"+str(r.vitesse)+" angle:"+str(r.angle))
    T.supprimerObjet(int(r.y),int(r.x))
    r.avance(temps)
    T.ajout_objet(r,int(r.y),int(r.x))
    print("stop tour t:"+str(temps))
    print("x:"+str(r.x)+" y:"+str(r.y)+" vitesse:"+str(r.vitesse)+" angle:"+str(r.angle))

if __name__ == '__main__':
    print("Initialisation Terrain")
    T = Terrain.Terrain(7,7)
    T.affichage()
    print("Initialisation Robot")
    r = Robot.Robot(3,3,1,45.)
    vAdapt = r.vecteurDeplacement.rotation(r.angle)
    T.ajout_objet(r,int(vAdapt.x),int(vAdapt.y))
    T.ajout_objet(r,int(r.x),int(r.y))
    print("x:"+str(r.x)+" y:"+str(r.y)+" vitesse:"+str(r.vitesse)+" angle:"+str(r.angle))
    for t in range(0,4):
        majAffichageRobot(t)
        T.affichage()
