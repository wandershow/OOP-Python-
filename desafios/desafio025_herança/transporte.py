from abc import ABC, abstractmethod


class Transporte(ABC):

    def __init__(self, distancia):
        if distancia <= 0:
            raise ValueError("A distância deve ser maior que zero.")
        self.distancia = distancia

    @abstractmethod
    def calcula_frete(self):
        pass

    def __str__(self):
        nome = type(self).__name__
        return f"Frete de {nome} para {self.distancia}km: R$ {self.calcula_frete():.2f}"
