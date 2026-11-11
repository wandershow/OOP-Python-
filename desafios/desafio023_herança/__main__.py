from poligono import Poligono
from quadrado import Quadrado
from circulo import Circulo


def main():

    q1 = Quadrado(12)
    q1.perimetro()
    q1.area()

    c1 = Circulo(20)
    c1.perimetro()
    c1.area()


if __name__ == "__main__":
    main()
