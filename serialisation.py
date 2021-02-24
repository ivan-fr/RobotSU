import pickle
from models import TerrainContinu, Robot, Polygone, Vecteur
import math

def creerCarteCarree():
    with open('carteCarree', 'wb') as f:
        tc = TerrainContinu.TerrainContinu([Vecteur.Vecteur(10,0), Vecteur.Vecteur(0,10), Vecteur.Vecteur(-10,0), Vecteur.Vecteur(0,-10)], Robot.Robot(5,5,0,90))
        pickle.dump(tc, f)

def ouvrirCarteCarree():
    with open('carteCarree', 'rb') as f:
        carte = pickle.load(f)
    return carte

def creerCarteTriangle():
    with open('carteTriangle', 'wb') as f:
        tc = TerrainContinu.TerrainContinu([Vecteur.Vecteur(10,0), Vecteur.Vecteur(-10,sqrt(2000)), Vecteur.Vecteur(-10,0)], Robot.Robot(2,2,0,90))
        pickle.dump(tc, f)

def ouvrirCarteTriangle():
    with open('carteTriangle', 'rb') as f:
        carte = pickle.load(f)
    return carte

def creerCarteRectanglePerso(x,y):
    with open('carteRectanglePerso', 'wb') as f:
        tc = TerrainContinu.TerrainContinu([Vecteur.Vecteur(x,0), Vecteur.Vecteur(0,y), Vecteur.Vecteur(-x,0), Vecteur.Vecteur(0,y)], Robot.Robot(x//2,y//2,0,90))
        pickle.dump(tc, f)

def ouvrirCarteRectanglePerso():
    with open('carteRectanglePerso', 'rb') as f:
        carte = pickle.load(f)
    return carte