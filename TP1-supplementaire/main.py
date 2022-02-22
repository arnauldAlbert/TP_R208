import sys
import Point as point
import Cercle as cercle
import Rectangle as rect
def main():
    p1 = point.Point(1,0)
    p2 = point.Point()

    print(p1)
    print(p2)


    print(f"distance = {p1.distance_coordonée(1,5)}")
    print(f"distance = {p2.distance_point(p1)}")
    
    c3 = cercle.Cercle(5)
    print(c3)

    c1 = cercle.Cercle(5,p1)
    print(c1)

    print(f"diametre {c1.diametre()}")

    print(f"surface {c3.surface()}")

    print(f"perimetre {c1.perimetre()}")

    if c1.contient(p1):
        print(f"{p1} appartient au {c1}")
    else:
        print(f"{p1} n'appartient pas au {c1}")

    p3 = point.Point(12,23)
    if c1.contient(p3):
        print(f"{p3} appartient au {c1}")
    else:
        print(f"{p3} n'appartient pas au {c1}")

    rect1 = rect.Rectangle(p1,2,5)
    print(rect1)
    print (f"point bas droit {rect1.point_bas_droit()}")
    print(f"point haut gauche {rect1.point_haut_gauche()}")
    print(f"point haut droit {rect1.point_haut_droit()}")

    print (f"perimetre du rectangle {rect1.perimetre()}")
    print (f"surface du rectangle {rect1.surface()}")

    if rect1.contient(p3):
        print(f"{p3} appartient à {rect1}")
    else :
        print(f"{p3} n'appartient pas à {rect1}")

    p4 = point.Point(2,3)
    if rect1.contient(p4):
        print(f"{p4} appartient à {rect1}")
    else:
        print(f"{p4} n'appartient pas à {rect1}")

if __name__ == "__main__":
    sys.exit(main())