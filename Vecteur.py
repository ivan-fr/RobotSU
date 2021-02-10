from math import sqrt, cos, sin, radians, acos, degrees

class Vecteur(object):
    """
    Vecteur du plan : 2 dimensions
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """
        -> str
        Permet de retourner une chaine de caractère représentant le vecteur
        """
        return "("+str(self.x)+","+str(self.y)+")"

    def norme(self):
        """
        -> float
        Retourne la norme du vecteur
        """
        return sqrt(self.x ** 2 + self.y ** 2)

    def __add__(self, autreVecteur):
        """
        Vecteur -> Vecteur
        Retourne un vecteur résultant de la somme du vecteur instance avec un autre vecteur
        """
        if not isinstance(autreVecteur, Vecteur):
            raise ValueError("L'Operande n'est pas une instance de la classe Vecteur")
        else:
            return Vecteur(self.x + autreVecteur.x, self.y + autreVecteur.y)

    def __mul__(self, scal):
        """
        Number -> Vecteur
        Retourne un vecteur résultant du produit du vecteur instance avec un scalaire
        """
        if (isinstance(scal, int) and not isinstance(scal, bool)) or isinstance(scal, float):
            return Vecteur(self.x * scal, self.y * scal)
        else:
            raise ValueError("L'Operande n'est pas un scalaire")

    def rotation(self, angle):
        """retourne le vecteur deplacement"""
        if not isinstance(angle, float) and (not isinstance(angle, int) or isinstance(angle, bool)):
            raise ValueError("L'Operande n'est pas un angle")

        vx = self.x * cos(radians(angle)) - self.y * sin(radians(angle))
        vy = self.x * sin(radians(angle)) + self.y * cos(radians(angle))

        return Vecteur(vx, vy)

    def get_sym_x_axis(self):
        """
        retourne le vecteur symetrique par rapport à l'axe des abscisses
        """
        return Vecteur(self.x, -self.y)
    
    def angle_entre(self, autreVecteur):
        """ Vecteur -> Float
        Permet de retourner l'angle entre deux vecteurs (en degrés)
        """
        prod = self.x * autreVecteur.x + self.y * autreVecteur.y
        cos_angle = prod/(self.norme() * autreVecteur.norme())
        return degrees(acos(cos_angle))

    def collision(self,pos1,autreVecteur,pos2):
        """ Tuple(x1,y1) * Vecteur * Tuple(x2,y2) -> Boolean
        Permet de dire s'il y a collision entre deux vecteurs
        """
        ax = pos1[0]
        ay = pos1[1]
        bx = pos1[0] + self.x
        by = pos1[1] + self.y
        cx = pos2[0]
        cy = pos2[1]
        dx = pos2[0] + autreVecteur.x
        dy = pos2[1] + autreVecteur.y

        ab_pv_ac = ((bx-ax)*(cy-ay))-((by-ay)*(cx-ax))
        ab_pv_ad = ((bx-ax)*(dy-ay))-((by-ay)*(dx-ax))
        test1 = ab_pv_ac * ab_pv_ad
        
        cd_pv_ca = ((dx-cx)*(ay-cy))-((dy-cy)*(ax-cx))
        cd_pv_cb = ((dx-cx)*(by-cy))-((dy-cy)*(bx-cx))
        test2 = cd_pv_ca * cd_pv_cb

        if test1 < 0 and test2 < 0:
            return True
        else:
            return False

    def collision1(self,pos1,autreVecteur,pos2):
        """ Tuple(x1,y1) * Vecteur * Tuple(x2,y2) -> Boolean
        Permet de dire s'il y a collision entre deux vecteurs
        """
        ab_pv_ac = ((pos1[0] + self.x-pos1[0])*(pos2[1]-pos1[1]))-((pos1[1] + self.y-pos1[1])*(pos2[0]-pos1[0]))
        ab_pv_ad = ((pos1[0] + self.x-pos1[0])*(pos2[1] + autreVecteur.y-pos1[1]))-((pos1[1] + self.y-pos1[1])*(pos2[0] + autreVecteur.x-pos1[0]))
        test1 = ab_pv_ac * ab_pv_ad
        
        cd_pv_ca = ((pos2[0] + autreVecteur.x-pos2[0])*(pos1[1]-pos2[1]))-((pos2[1] + autreVecteur.y-pos2[1])*(pos1[0]-pos2[0]))
        cd_pv_cb = ((pos2[0] + autreVecteur.x-pos2[0])*(pos1[1] + self.y-pos2[1]))-((pos2[1] + autreVecteur.y-pos2[1])*(pos1[0] + self.x-pos2[0]))
        test2 = cd_pv_ca * cd_pv_cb

        if test1 < 0 and test2 < 0:
            return True
        else:
            return False
