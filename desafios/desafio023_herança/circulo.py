from poligono import Poligono
import math
from rich import print


class Circulo(Poligono):

    def __init__(self, raio):
        super().__init__(0)
        self.raio = raio

    def perimetro(self):
        perimetro = 2 * math.pi * self.raio
        print(f"Perimetro do Circulo: {perimetro:.2f}")

    def area(self):
        area = math.pi * (self.raio * self.raio)
        print(f"Area do Circulo: {area:.2f}²")
