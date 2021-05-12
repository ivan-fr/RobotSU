from models import Robot
from controllers import StrategieTourner, StrategieAvancerDroit
import datetime
import numpy as np
from PIL import Image
import math
import time

def get_min_col_from_max_g_and_b(array):
    array_adapted = np.zeros((array.shape[0] + 2,))
    array_adapted[1:-1] = array
    zeros_index = np.where(array_adapted == 0)[0]
    diff = zeros_index[1:] - zeros_index[:-1]
    return int(array_adapted[zeros_index[np.argmax(diff)]+1]), np.max(diff) - 1

def detectBalise(image):
    data = np.asarray(image)
    colors = ("r", "g", "b")
    channel_ids = (0, 1, 2)

    # create the histogram plot, with three lines, one for
    # each color
    #plt.xlim([0, data.shape[1]])
    histograms = []

    for channel_id, c in zip(channel_ids, colors):
        if channel_id == 0:
            logical = (data[:, :, 0] > 30) & \
              (data[:, :, 1] < data[:, :, 0]) & \
               (data[:, :, 2] < data[:, :, 0])
        elif channel_id == 2:
            logical = (data[:, :, 2] > 30) & \
              (data[:, :, 1] < data[:, :, 2]) & \
               (data[:, :, 0] < data[:, :, 2])
        else:
            logical = (data[:, :, 1] > 30) & \
              (data[:, :, 0] < data[:, :, 1]) & \
               (data[:, :, 2] < data[:, :, 1])

        _, col = np.where(logical)
        histogram, bin_edges = np.histogram(
        col, bins=data.shape[1], range=(0, data.shape[1])
        )
        histograms.append(histogram)
        #plt.plot(bin_edges[:-1], histogram, color=c)

    histo_r, histo_g, histo_b = histograms

    r_and_g = np.where((histo_g[:] > 40) & (histo_b[:] > 50), 1, 0)
    more_r_than_blue = histo_r[:] > histo_b[:]
    r_and_g_col = np.where(r_and_g != 0)[0]

    diff_close = r_and_g_col[1:] - r_and_g_col[:-1]
    r_and_g_col = np.where(diff_close <= 10, r_and_g_col[1:], 0)

    col_min, length = get_min_col_from_max_g_and_b(r_and_g_col)

    balise = False

    if length > data.shape[1] * 0.08:
        balise_b = more_r_than_blue[col_min-int(length*.94):col_min-1]

        if balise_b.size > 0:
            balise = np.all(balise_b)
        else:
            balise = False

    #balise in front
    baliseInFront = False
    itIsLeft = None
    pourcentage = None

    if balise:
        colonne_midle = data.shape[1] // 2
        baliseInFront = abs(colonne_midle - col_min) <= 50

        if not baliseInFront:
            itIsLeft = col_min < colonne_midle
            pourcentage = abs(col_min -
                              colonne_midle) / colonne_midle

    #plt.xlabel("colonnes")
    #plt.ylabel("quantite RGB")
    #plt.show()
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
