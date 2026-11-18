from transporte import Transporte
from rich import print


class Moto(Transporte):

    FATOR = 1.0
    FRETE_MINIMO = 5.0


    def calcula_frete(self):
        return max(self.distancia * self.FATOR, self.FRETE_MINIMO)

    