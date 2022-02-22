""" classe d'un cercle. cet objet est défini par son centre et son rayon
    centre : Point
    rayon : réel
"""
import Point as point

class Cercle:

    def __init__(self, rayon, centre=point.Point(0,0)):
        self.__rayon = rayon
        self.__centre = centre

    @classmethod
    def constructeur_avec_point(cls,rayon,point):
        return cls(rayon, point)

    @classmethod
    def constructeur_avec_coordonees(cls,rayon, x, y):
        return cls(rayon, point.Point(x,y))

    def __str__(self):
        return f"Cercle de centre {self.__centre} et de rayon {self.__rayon}"
