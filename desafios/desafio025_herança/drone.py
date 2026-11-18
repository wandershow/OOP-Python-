from transporte import Transporte
from rich import print


class Drone(Transporte):

    def __init__(self, distancia):
        super().__init__(distancia)
        self.frete = "Drone"
        self.fator = 9.50
        self.valor = 0

    def calcula_frete(self):
        if self.distancia > 10:
            return print("distância maior que o raio permitido de 10 km")
        else:
            self.valor = self.distancia * self.fator
            return self.valor
