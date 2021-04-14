from models import Robot
from controllers import StrategieTourner, StrategieAvancerDroit
import datetime
import numpy as np
from PIL import Image
import math
import time

img_i = 0

def select(data, R, G, B):
    data_copy = data.copy()
    data_copy[:, :, 2] = np.select([B], [data_copy[:, :, 2]])
    data_copy[:, :, 1] = np.select([G], [data_copy[:, :, 1]])
    data_copy[:, :, 0] = np.select([R], [data_copy[:, :, 0]])
    data_copy[np.any(data_copy[:, :] == 0, axis=2)] = [0, 0, 0]
    return data_copy


def distance(data, ligne, colonne):
    ligne_c, colonne_c, _ = data.shape
    ligne_c = ligne_c // 2
    colonne_c = colonne_c // 2
    return ((ligne_c - ligne) ** 2 + (colonne_c - colonne) ** 2) ** (.5)


def detectBalise(data):
    img = Image.fromarray(data)
    img.save("../images/capture_" + img_i + ".jpg")
    img_i += 1

    R = np.logical_and(10 < data[:, :, 0], data[:, :, 0] < 35)
    G = np.logical_and(80 < data[:, :, 1], data[:, :, 1] < 100)
    B = np.logical_and(160 < data[:, :, 2], data[:, :, 2] < 180)

    image_blue = select(data, R, G, B)
    R = np.logical_and(40 < data[:, :, 0], data[:, :, 0] < 65)
    G = np.logical_and(130 < data[:, :, 1], data[:, :, 1] < 145)
    B = np.logical_and(100 < data[:, :, 2], data[:, :, 2] < 120)

    image_green = select(data, R, G, B)
    R = np.logical_and(180 < data[:, :, 0], data[:, :, 0] < 190)
    G = np.logical_and(60 < data[:, :, 1], data[:, :, 1] < 75)
    B = np.logical_and(65 < data[:, :, 2], data[:, :, 2] < 75)

    image_red = select(data, R, G, B)
    lignes_b, colonnes_b = np.where(image_blue[:, :, 0] != 0)
    lignes_g, colonnes_g = np.where(image_green[:, :, 0] != 0)
    lignes_r, colonnes_r = np.where(image_red[:, :, 0] != 0)

    # balise on image
    avg_c_r = np.average(colonnes_r)
    avg_c_b = np.average(colonnes_b)
    avg_c_g = np.average(colonnes_g)
    avg_l_g = np.average(lignes_g)
    avg_l_b = np.average(lignes_b)
    avg_l_r = np.average(lignes_r)
    balise = avg_c_r <= avg_c_b and (
        np.min(lignes_b) <= avg_l_r <= np.max(lignes_b))
    balise = balise and (np.min(colonnes_b) <= avg_c_g <=
                         np.max(colonnes_b)) and avg_l_g <= avg_l_b

    #balise in front
    baliseInFront = False
    itIsLeft = None
    pourcentage = None

    if balise:
        colonne_c = data.shape[1] // 2
        dist_corner = distance(data, 0, 0)
        dist_r = .2 <= (distance(data, avg_l_r, avg_c_r) / dist_corner) <= .6
        dist_g = .2 <= (distance(data, avg_l_g, avg_c_g) / dist_corner) <= .6
        dist_b = .2 <= (distance(data, avg_l_b, avg_c_b) / dist_corner) <= .6
        baliseInFront = balise and dist_r and dist_b and dist_g
        baliseInFront = baliseInFront and avg_c_b > colonne_c and avg_c_r < colonne_c and avg_c_g > colonne_c

        if not baliseInFront:
            itIsLeft = avg_c_b < colonne_c
            pourcentage = abs((avg_c_b + avg_c_r) / 2. -
                              colonne_c) / colonne_c

    return balise, baliseInFront, itIsLeft, pourcentage


class StrategieSuivreBalise(object):
    def __init__(self, stratAvancer, stratTourner):
        self.liste_strategies = [stratTourner] * int(360 / stratTourner.angleTarget)

        self.dps_base = self.liste_strategies[0].degreParSeconde
        self.angleTarget_base = self.liste_strategies[0].angleTarget

        self.stratAvancer = stratAvancer
        self.i_liste_strategies = -1
        self.baliseInFront = False
        self.modeTourner = False

    def start(self):
        self.i_liste_strategies = -1
        self.baliseInFront = False
        self.modeTourner = False
        self.stratAvancer.start()

    def start_basic_tourner(self):
        self.i_liste_strategies += 1
        self.liste_strategies[self.i_liste_strategies].start()
        self.modeTourner = True
        self.step_tourner()

    def step_tourner(self):
        if not self.liste_strategies[self.i_liste_strategies].stop():
            self.liste_strategies[self.i_liste_strategies].step()
        else:
            self.modeTourner = False

    def step(self):
        if self.stop():
            return

        if self.modeTourner:
            self.step_tourner()
        elif not self.baliseInFront:
            time.sleep(1)
            balise, baliseInFront, itIsLeft, pourcentage = detectBalise(self.stratAvancer.wrapper.get_image())
            print("balise in image ?", balise, "balise on front ?", baliseInFront)
            time.sleep(1)
            if balise:
                if baliseInFront:
                    self.stratAvancer.step()
                    self.baliseInFront = True
                else:
                    new_angleTarget = (self.angleTarget_base / 2) * pourcentage
                    new_dps = abs(self.dps_base) * pourcentage
                    
                    self.liste_strategies[self.i_liste_strategies].start()
                    self.liste_strategies[self.i_liste_strategies].angleTarget = new_angleTarget

                    if itIsLeft:
                        self.liste_strategies[self.i_liste_strategies].degreParSeconde = new_dps
                    else:
                        self.liste_strategies[self.i_liste_strategies].degreParSeconde = - new_dps

                    self.modeTourner = True
                    self.step_tourner()
            else:
                self.start_basic_tourner()
        else:
            self.stratAvancer.step()

    def stop(self):
        # condition d'arret lorsque le robot a parcouru les 4 cotes
        try:
            _ = self.liste_strategies[self.i_liste_strategies + 1]
            return self.stratAvancer.stop()
        except IndexError:
            return True
