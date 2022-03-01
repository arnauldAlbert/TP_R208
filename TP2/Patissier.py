import Patisserie

class Patissier:

    def __init__(self, nom="", prenom=""):
        self.__nom = nom
        self.__prenom = prenom
        self.__liste_patisserie = []

    def __str__(self):
        msg=f"Patissier {self.__nom} {self.__prenom} propose les patisseries : \n"
        for p in self.__liste_patisserie:
            msg = msg +  p.__str__() + "\n"
        return msg

    def creer_patisserie(self,poids=0, categorie=None):
        p = Patisserie.Patisserie(poids,categorie)
        p.set_createur2(self.__nom)
        if p not in self.__liste_patisserie:
            self.__liste_patisserie.append(p)

    def trier_patisseries(self):
        for i in range(len(self.__liste_patisserie)-1):
            for j in range(len(self.__liste_patisserie)-1):
                if self.__liste_patisserie[j].get_poids() > self.__liste_patisserie[j+1].get_poids():
                    temp = self.__liste_patisserie[j]
                    self.__liste_patisserie[j] = self.__liste_patisserie[j+1]
                    self.__liste_patisserie[j + 1] = temp
            if self.__est_trier():
                break

    def __est_trier(self):
        for i in range(len(self.__liste_patisserie)-1):
            if self.__liste_patisserie[i].get_poids() > self.__liste_patisserie[i+1].get_poids():
                return False
        return True