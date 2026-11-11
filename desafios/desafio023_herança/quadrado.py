from poligono import Poligono


class Quadrado(Poligono):

    def __init__(self, tamanho_lado):
        super().__init__(4)
        self.tamanho_lado = tamanho_lado

    def perimetro(self):
        perimetro = self.qtd_lados * self.tamanho_lado
        print(f"Perimetro do Quadrado: {perimetro}")

    def area(self):
        area = self.tamanho_lado * self.tamanho_lado
        print(f"Area do Quadrado: {area}²")
