import Terrain as T
    
if __name__ == '__main__':
    print("Terrain de 30x30 contenant 30 objets placés aléatoirement")
    t = T.Terrain(30, 60)
    t.ajout_alea(40)
    t.affichage()

