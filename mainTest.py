from views import Terrain
from models import TerrainContinu
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
    tc = TerrainContinu.Carre(20, (10, 1))
    controleur = Controleur.Controleur(tc.robot,tc)
    for i in range(4) :
        t = Terrain.construireTerrain(tc, 0.2)
        #permet d'avancer
        controleur.update()
        #permet de tourner
        controleur.update()
        t.affichage()
        t.supprimerAffichage()

    # affichage = AffichageThread.AffichageThread(tc)
    # t1 = threading.Thread(target = affichage.update())
    # t2 = threading.Thread(target = Deplacement_Carre())
    # t1.start()
    # t2.start()