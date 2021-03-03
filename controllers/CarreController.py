from views import Terrain
from models import TerrainContinu, Robot, Polygone
from controllers import StrategieCarre
import threading 
import time
# import AffichageThread

# def Deplacement_Carre(self):
#     for i in range(0,4) :
#         #permet d'avancer
#         controleur.update()
#         #permet de tourner
#         controleur.update()
#         Terrain.affichage()

lock = threading.RLock()

def affichage(tc, fps):
    while True:
        with lock:
            t = Terrain.construireTerrain(tc, 0.5)
            t.affichage()
            t.supprimerAffichage()
            time.sleep(1./fps)

def updateModele(stratCarre, fps):
    while not stratCarre.stop:
        with lock:
            stratCarre.step()
            time.sleep(1./fps)

def run():
    tc = TerrainContinu.Carre(20)
    tc.ajoutPolygone(Polygone.hexagone((0, 0), 5))
    tc.robot = Robot.Robot(1,7, 1, 0.)
    # mache avec 0 ou 180
    tc.robot.rotation(0)
    # mache avec 90 ou -90 comme valeur de rotation, entier positif pour distance
    stratCarre = StrategieCarre.StrategieCarre(tc, 7.)
    #--> pour pouvoir faire des carres dans des sens differents
    stratCarre.start()

    fps = 1

    t1 = threading.Thread(target = affichage, args=(tc, fps))
    t2 = threading.Thread(target = updateModele, args=(stratCarre, fps))
    t1.start()
    t2.start()
