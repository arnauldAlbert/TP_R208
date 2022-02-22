class Voiture:
    def __init__(self, marque="Peugeot", modele="None", couleur="rouge", chevaux = 0):
        self.__marque = marque # attribut devenu privé avec le __ devant le nom de l'attribut
        self.__modele = modele
        self.__chevaux = chevaux
        self.__couleur = couleur
        self.__options = []

    def get_modele(self):
        return self.__modele

    def set_modele(self,modele):
        self.__modele = modele

    def get_marque(self):
        return self.__marque

    def set_marque(self, marque):
        self.__marque = marque

    def get_chevaux(self):
        return self.__chevaux

    def set_chevaux(self, chevaux):
        self.__chevaux = chevaux

    def get_couleur(self):
        return self.__couleur

    def set_couleur(self, couleur):
        self.__couleur= couleur

    def get_options(self):
        return self.__options

    def set_options(self, options):
        self.__options = options

    def add_option(self,option):
        self.__options.append(option)

    def remove_option(self,option):
        self.__options.remove(option)

    def is_option(self,option):
        if option in self.__options:
            return True
        else:
            return False

    def __str__(self):
        msg =f"voiture de marque {self.__marque} de modéle {self.__modele} avec {self.__chevaux} chevaux et de couleur {self.__couleur} et les options suivantes: \n"
        for op in self.__options:
            msg = msg + f" - {op} \n"
        return msg