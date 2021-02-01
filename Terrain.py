import random 
class Terrain(object):
    def __init__(self, nbLignes, nbColonnes):
        self.nbLignes = nbLignes
        self.nbColonnes = nbColonnes
        self.grille = self.creerGrille()

    def creerGrille(self):
        """
        Retourne la grille du terrain, cad un tableau de tableau (remplis de None=vide)
        """
        return [[None] * self.nbColonnes] * self.nbLignes
    
    
    def casevide(self, x, y, grille):
        """ int * int * tab [][] -> boolean
        retourne vrai si la case est vide, et faux si celle-ci est occupee"""
        if x > self.nbLignes or y > self.nbColonnes:
            print("cette case n'est pas dans le tableau")
            return False
        if grille[x][y] is None:
            return True
        return False

    def ajout_objet(self,item,x,y) : 
        """tab[][] * Object * int *int ->boolean
        Place un objet donné en argument dans la case[x][y] du terrain en verifiant s'il est vide."""
        if(self.casevide(x,y,grille)):
            grille[x][y]==item
            return True
        return False


    def ajout_alea(self,item,nbitem):
        """tab[][] * Object * int -> None
        Place item nbfois aleatoirement sur le Terrain."""
        x=0
        while(x<nbitem):
            a=random.randint(0, self.nbLignes)
            b=random.randint(0, self.nbColonnes)
            while(self.casevide(a,b,grille)==False) : 
                a=random.randint(0, self.nbLignes)
                b=random.randint(0, self.nbColonnes)
            self.ajout_objet(item,a,b)
            x=x+1
        
    def affichage(self):
        """affiche le Terrain"""
        for i in self.grille:
            print("|",end="")
            for j in i:
                print(j,end="")
                print(" | ", end="")
            print()
