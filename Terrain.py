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
        return [[None] * self.nbColonnes for _ in range(self.nbLignes)]
    
    
    def casevide(self, x, y):
        """ int * int * tab [][] -> boolean
        retourne vrai si la case est vide, et faux si celle-ci est occupee"""
        if x > self.nbLignes or y > self.nbColonnes:
            return False
        if self.grille[x][y] is None:
            return True
        return False

    def ajout_objet(self,item,x,y) : 
        """Object * int *int ->boolean
        Place un objet donné en argument dans la case[x][y] du terrain en verifiant s'il est vide."""
        if(self.casevide(x,y)):
            self.grille[x][y]=item
            return True
        return False


    def ajout_alea(self,item,nbitem):
        """Object * int -> None
        Place item nbfois aleatoirement sur le Terrain."""
        for _ in range(nbitem):
            a=random.randint(0, self.nbLignes)
            b=random.randint(0, self.nbColonnes)
            while(self.casevide(a,b)==False) : 
                a=random.randint(0, self.nbLignes)
                b=random.randint(0, self.nbColonnes)
            self.ajout_objet(item,a,b)
        
    def affichage(self):
        """affiche le Terrain"""
        bordure="".join(["+","-" * self.nbColonnes,"+"])
        print(bordure)
        for i in self.grille:
            print("|",end="")
            for j in i:
                if j is None:
                    print(" ", end="")
                else:
                    print("X", end="")
            print("|",end="")
            print()
        print(bordure+"\n")
