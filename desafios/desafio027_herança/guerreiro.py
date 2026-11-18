from personagem import Personagem


class Guerreiro(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida, ["Espadada", "Golpe de escudo", "Investida"])

    def curar(self):
        ...  # você implementa