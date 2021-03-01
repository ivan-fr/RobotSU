from views import Terrain
from models import TerrainContinu, Robot, Polygone
import Controleur
import threading 
# import AffichageThread

# def Deplacement_Carre(self):
#     for i in range(0,4) :
#         #permet d'avancer
#         controleur.update()
#         #permet de tourner
#         controleur.update()
#         Terrain.affichage()


if __name__ == '__main__':
    tc = TerrainContinu.Carre(20)
    tc.ajoutPolygone(Polygone.hexagone((0, 0), 5))
    tc.robot = Robot.Robot(1,7, 1, 0.)
    # mache avec 0 ou 180
    tc.robot.rotation(0)
    # mache avec 90 ou -90 comme valeur de rotation, entier positif pour distance
    controleur = Controleur.Controleur(tc.robot,tc, -90, 7)
    #--> pour pouvoir faire des carres dans des sens differents

    #position initiale du robot
    pos_x = tc.robot.x
    pos_y = tc.robot.y
    # condition d'arret : revenu a meme position -> au debut, meme position, donc flag
    init = True
    # for i in range(5):
    while (abs(pos_x - tc.robot.x) > 0.00001) or (abs(pos_y - tc.robot.y) > 0.00001) or init : #-> manque une iteration 
        # print(abs(pos_x - tc.robot.x) > 0.00001 or abs(pos_y - tc.robot.y) > 0.00001 or init, pos_x, tc.robot.x, pos_y, tc.robot.y, init)
        t = Terrain.construireTerrain(tc, 1)
        #permet d'avancer
        controleur.update()
        #permet de tourner
        controleur.update()
        t.affichage()
        t.supprimerAffichage()
        init = False
    print(abs(pos_x - tc.robot.x) < 0.00001 or abs(pos_y - tc.robot.y) < 0.00001 or init, pos_x, tc.robot.x, pos_y, tc.robot.y, init)

        # --> PB PREMIER DEPLACEMENT

    # affichage = AffichageThread.AffichageThread(tc)
    # t1 = threading.Thread(target = affichage.update())
    # t2 = threading.Thread(target = Deplacement_Carre())
    # t1.start()
    # t2.start()