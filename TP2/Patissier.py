import Patisserie

class Patissier:

    def __init__(self, nom="", prenom=""):
        self.__nom = nom
        self.__prenom = prenom
        self.__liste_patisserie = ()

    def __str__(self):
        msg=f"Patissier {self.__nom} {self.__prenom} propose les patisseries : \n"
        for p in self.__liste_patisserie:
            msg = msg +  p.__str__() + "\n"

    def creer_patisserie(self,poids=0, categorie=None):
        p = Patisserie.Patisserie(poids,categorie)
        p.set_createur2(self.__nom)
        if p not in self.__liste_patisserie:
            self.__liste_patisserie.append(p)
