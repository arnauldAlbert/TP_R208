import Point as pt

class Rectangle:
    def __init__(self,pointBG=pt.Point(), longueur=1, largeur =1):
        self.__pointBG = pointBG
        self.__largeur = largeur
        self.__longueur = longueur

    @classmethod
    def const_points(cls,pointBG, pointHD):
        longueur = pointHD.__x - pointBG.__x
        largeur = pointHD.__y - pointBG.__y
        return cls(pointBG,longueur,largeur)

    def __str__(self):
        return f"rectangle de coin bas gauche {self.__pointBG} de longueur horizontale {self.__longueur} et de largeur verticale {self.__largeur}"

    def surface(self):
        return self.__largeur*self.__longueur

    def perimetre(self):
        return 2*(self.__longueur+self.__largeur)

    def point_bas_gauche(self):
        return self.__pointBG

    def point_bas_droit(self):
        x = self.__pointBG.get_x()+self.__longueur
        y = self.__pointBG.get_y()
        return pt.Point(x,y)

    def point_haut_gauche(self):
        x = self.__pointBG.get_x()
        y = self.__pointBG.get_y()+self.__largeur
        return pt.Point(x, y)

    def point_haut_droit(self):
        x = self.__pointBG.get_x()+self.__longueur
        y = self.__pointBG.get_y()+self.__largeur
        return pt.Point(x, y)

    def contient(self,p):
        res = False
        if (self.__pointBG.get_x() <= p.get_x() <= self.__pointBG.get_x()+self.__longueur) and \
            (self.__pointBG.get_y() <= p.get_y() <= self.__pointBG.get_y()+self.__largeur):
            res = True
        return res