import Voiture as maVoiture
import sys
def main():
    # test des deux constructeurs
    myCar = maVoiture.Voiture("Renault", "Alpine",450, "bleue")
    myCar2 = maVoiture.Voiture()

    # test de la fonction __str__
    print(myCar)

    # test des assesseurs en lecture
    print(f"ma Voiture est {myCar2.get_marque()} {myCar2.get_modele()} ")

    # test des assesseurs en écritures
    myCar2.set_marque("Toyota")
    myCar2.set_modele("308")
    myCar2.set_chevaux(110)
    myCar.set_couleur("gris")
    print(f"ma Voiture est {myCar2.get_marque()} {myCar2.get_modele()} de couleur {myCar2.get_couleur()} et avec {myCar2.get_chevaux()} chevaux")

    # test de la fonction qui ajoute des options
    myCar.add_option("airbag")
    myCar.add_option("jantes alu")
    myCar.add_option("siéges cuir")

    print(myCar)

    myCar2.add_option("siéges cuir")
    print(myCar2)

    # test de présence d'une option
    if myCar.is_option("airbag"):
        print(f"ma voiture {myCar.get_modele()} posséde un airbag")
    else :
        print(f"ma voiture {myCar.get_modele()} ne posséde pas un airbag")

    #test de la fonction de suppression d'option
    myCar.remove_option("airbag")

    if myCar.is_option("airbag"):
        print(f"ma voiture {myCar.get_modele()} posséde un airbag")
    else:
        print(f"ma voiture {myCar.get_modele()} ne posséde pas un airbag")


if __name__ == "__main__":
    sys.exit(main())