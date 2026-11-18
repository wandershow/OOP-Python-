from transporte import Transporte
from rich import print


class Caminhao(Transporte):

    FATOR = 1.20
    DISTANCIA_MINIMA = 50

    def __init__(self, distancia):
        if distancia < self.DISTANCIA_MINIMA:
            raise ValueError(
                f"Caminhão só atende a partir de {self.DISTANCIA_MINIMA} km."
            )
        super().__init__(distancia)

    def calcula_frete(self):
        return self.distancia * self.FATOR
