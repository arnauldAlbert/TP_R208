import sys
import Point as point
import Cercle as cercle
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




if __name__ == "__main__":
    sys.exit(main())