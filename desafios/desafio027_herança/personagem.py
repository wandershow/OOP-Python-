import random
from abc import ABC, abstractmethod


class Personagem(ABC):

    def __init__(self, nome, vida, golpes):
        self.nome = nome
        self.vida = vida
        self.vida_maxima = vida
        self.golpes = golpes

    def esta_vivo(self):
        return self.vida > 0

    def atacar(self, alvo, forca):
        if not self.esta_vivo():
            print(f"{self.nome} está derrotado e não pode atacar!")
            return
        golpe = random.choice(self.golpes)
        dano = random.randint(forca // 2, forca)
        print(f"{self.nome} usou {golpe} em {alvo.nome}!")
        alvo.receber_dano(dano)

    def receber_dano(self, dano):
        self.vida = max(self.vida - dano, 0)
        print(f"{self.nome} sofreu {dano} de dano. Vida: {self.vida}/{self.vida_maxima}")
        if not self.esta_vivo():
            print(f"{self.nome} foi derrotado!")

    @abstractmethod
    def curar(self):
        pass