"""
    Classe Point :
        cette classe posséde 2 attributs privés, les coordonnées du Point
        x : abscissse
        y : l'ordonnée
    """
import math
class Point:

    def __init__(self,x=0,y=0):
        """
        le constructeur complet.
        les valeurs par défaut donne le point origine du répére
        """
        self.__x = x
        self.__y = y

    def __str__(self):
        """ méthode d'affichage par défaut"""
        return f"Point ({self.__x},{self.__y})"

    def distance_coordonée(self,x,y):
        """ fonction de calcul d'une distance par rapport à des coordonées """
        calc = math.sqrt((x-self.__x)*(x-self.__x) + (y-self.__y)*(y-self.__y))
        return calc

    def distance_point(self,p):
        """ fonction de calcul d'une distance par rapport à un autre Point """
        calc = math.sqrt((p.__x-self.__x)*(p.__x-self.__x) + (p.__y-self.__y)*(p.__y-self.__y))
        return calc

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y