from personagem import Personagem


class Mago(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida, ["Bola de fogo", "Raio arcano", "Nevasca"])

    def curar(self):
        ...  # você implementa