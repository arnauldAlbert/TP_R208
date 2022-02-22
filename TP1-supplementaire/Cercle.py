""" classe d'un cercle. cet objet est défini par son centre et son rayon
    centre : Point
    rayon : réel
"""
import math

import Point as point

class Cercle:

    def __init__(self, rayon, centre=point.Point(0,0)):
        self.__rayon = rayon
        self.__centre = centre

    def __str__(self):
        return f"Cercle de centre {self.__centre} et de rayon {self.__rayon}"

    def diametre(self):
        return self.__rayon*2

    def perimetre(self):
        return self.__rayon*2*math.pi

    def surface(self):
        return math.pi*self.__rayon*self.__rayon

    def contient(self,p):
        if self.__centre.distance_point(p) <= self.__rayon:
            return True
        else:
            return False

    def intersection(self,c):
        if self.__centre.distance_point(c.__centre) < self.__rayon+c.__rayon \
            and self.__centre.distance_point(c.__centre) > max(self.__rayon,c.__rayon):
            return True
        else :
            return False