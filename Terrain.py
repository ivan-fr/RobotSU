import random 
import Robot

class Terrain(object):
    def __init__(self, nbLignes, nbColonnes):
        self.nbLignes = nbLignes
        self.nbColonnes = nbColonnes
        self.grille = self.creerGrille()

    def creerGrille(self):
        """
        -> list[list[NoneType]]
        Retourne la grille du terrain, cad un tableau multidimensionnel vide
        """
        return [[None] * self.nbColonnes for _ in range(self.nbLignes)]
    
    
    def casevide(self, x, y):
        """ int * int * tab [][] -> boolean
        retourne vrai si la case est vide, et faux si celle-ci est occupee"""
        if x >= self.nbLignes or x < 0 or y >= self.nbColonnes or y < 0:
            return False
        if self.grille[x][y] is None:
            return True
        return False

    def ajout_objet(self,objet,x,y) : 
        """Object * int *int ->boolean
        Place un objet donné en argument dans la case[x][y] du terrain en verifiant s'il est vide."""
        if(self.casevide(x,y)):
            self.grille[x][y]=objet 
            return True
        return False


    def ajout_alea(self,nbitem):
        """Object * int -> boolean
        Place item nbfois aleatoirement sur le Terrain."""
        if (self.nbLignes*self.nbColonnes > nbitem):
            for _ in range(nbitem):
                o=object()
                a=random.randint(0, self.nbLignes)
                b=random.randint(0, self.nbColonnes)
                while(self.casevide(a,b)==False) : 
                    a=random.randint(0, self.nbLignes)
                    b=random.randint(0, self.nbColonnes)
                self.ajout_objet(o,a,b)
            return True
        return False 

    def affichage(self):
        """affiche le Terrain"""
        bordure="".join(["+","-" * self.nbColonnes,"+"])
        print(bordure)
        for i in self.grille:
            print("|",end="")
            for j in i:
                if j is None:
                    print(" ", end="")
                elif isinstance(j, Robot.Robot):
                    print("R", end="")
                else:
                    print("X", end="")
            print("|",end="")
            print()
        print(bordure+"\n")

    def supprimerObjet(self, x, y):
        """int * int -> bool
        met la case à None"""
        if(x < 0 or y < 0 or x >= self.nbLignes or y >= self.nbColonnes):
            return False
        self.grille[x][y] = None
        return True
