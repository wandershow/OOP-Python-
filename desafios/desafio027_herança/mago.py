from personagem import Personagem
import random


class Mago(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida, ["Bola de fogo", "Raio arcano", "Nevasca"])

    def curar(self):
        if not self.esta_vivo():
            print(f"{self.nome} faleceu impossivel curar!")
            return
        vida_antes = self.vida
        cura = random.randomint(300, 600)
        self.vida = (self.vida + cura, self.vida_maxima)
        recuperado = self.vida - vida_antes
        print(
            f"{self.nome} usou uma poção para se curar de {recuperado}. Vida: {self.vida}/{self.vida_maxima}"
        )
