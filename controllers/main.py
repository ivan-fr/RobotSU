from views import Terrain
from models import TerrainContinu, Robot, Polygone
import StrategieCarre
import threading 
# import AffichageThread

# def Deplacement_Carre(self):
#     for i in range(0,4) :
#         #permet d'avancer
#         controleur.update()
#         #permet de tourner
#         controleur.update()
#         Terrain.affichage()

def affichage(tc):
    t = Terrain.construireTerrain(tc, 0.5)
    t.affichage()
    t.supprimerAffichage()

if __name__ == '__main__':
    tc = TerrainContinu.Carre(20)
    tc.ajoutPolygone(Polygone.hexagone((0, 0), 5))
    tc.robot = Robot.Robot(1,7, 1, 0.)
    # mache avec 0 ou 180
    tc.robot.rotation(0)
    # mache avec 90 ou -90 comme valeur de rotation, entier positif pour distance
    stratCarre = StrategieCarre.StrategieCarre(tc, 7)
    #--> pour pouvoir faire des carres dans des sens differents

    t1 = threading.Thread(target = affichage, args=(tc,))
    t1.start()

    stratCarre.start()

    while not stratCarre.stop:
        stratCarre.step()

