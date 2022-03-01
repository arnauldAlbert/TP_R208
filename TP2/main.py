import sys
import Patisserie as pa
import Patissier as pat
import pickle

def main():
    # test des deux constructeurs
    p1 = pa.Patisserie(250.6, "viennoiserie")
    print(p1)
    p2 = pa.Patisserie(250.6)
    p3 = pa.Patisserie(532.9, "gateau")
    p3.set_createur("Arnauld")
    p4 = pa.Patisserie(23.3,"viennoiserie")
    print(p1)
    print(p2)
    print(p3)
    print(p4)
    print(f"liste des categories autorisée {pa.Patisserie.categorie_autorise()}")
    if p1==p2:
        print ("les deux patisseries sont identiques")
    else:
        print("les deux patisseries sont différentes")

    p5 = p1+p4
    print (p5)

    fw = open("../files/data.pickle","wb")
    pickle.dump(p1,fw)
    fw.close()
    fr = open("../files/data.pickle","rb")
    p6 = pickle.load(fr)
    print (p6)

    p3.sauvegarder("../files/data2.pickle")
    p7= pa.Patisserie.chargementstatic("../files/data2.pickle")
    print (p7)

    toto = pat.Patissier("Arnauld","ALBERT")
    toto.creer_patisserie(250, "tarte")
    toto.creer_patisserie(230, "tarte")
    toto.creer_patisserie(289, "tarte")
    toto.creer_patisserie(120, "tarte")
    toto.creer_patisserie(1180, "tarte")

    print (toto)
    toto.trier_patisseries()
    print (toto)
if __name__ == "__main__":
        sys.exit(main())