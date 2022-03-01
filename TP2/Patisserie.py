import os
import pickle

class Patisserie:
    @staticmethod
    def categorie_autorise():
        return ("gateau", "tarte")

    __createur = "Ratatouille"

    def __init__(self, poids=0.0, categorie=None):
        self.__poids = poids
        self.__categorie = categorie

    def __str__(self):
        return f"Patisserie pesant {self.__poids} de type {self.__categorie} crée par {self.__createur}"

    def get_poids(self):
        return self.__poids

    def get_categorie(self):
        return self.__categorie

    def set_poids(self,poids):
        if type(poids) == float or type(poids) == int:
            self.__poids = poids
        else:
            print("la valeur saisie n'est pas un réel")

    def set_createur2(self, createur):
        self.__createur = createur

    def get_createur2(self):
        return self.__createur


    def set_categorie(self, categorie):
        self.__categorie = categorie

    @classmethod
    def set_createur(cls,createur):
        cls.__createur = createur

    @classmethod
    def get_createur(cls):
        return cls.__createur

    def __eq__(self, other):
        res = False
        if self.__poids == other.get_poids():
            res = True
        return res

    def __add__(self,other):
        categorie = None
        if self.__categorie == other.get_categorie():
            categorie = self.get_categorie()
        poids = self.__poids + other.get_poids()
        return Patisserie(poids,categorie)

    def sauvegarder(self,chemin):
       # if os.path.isfile(chemin):
        fw = open(chemin,"wb")
        pickle.dump(self,fw)


    def chargement(self,chemin):
      #  if os.path.isfile(chemin):
        fr = open(chemin, "rb")
        temp = pickle.load(fr)
        self.__poids = temp.get_poids()
        self.__categorie = temp.get_categorie()
        self.set_createur2 = temp.get_createur2()

    @staticmethod
    def chargementstatic(chemin):
        res = None
        if os.path.isfile(chemin):
            fr = open(chemin, "rb")
            res = pickle.load(fr)
        return res