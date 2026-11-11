from cafeteria import Cafeteria


class Cafe(Cafeteria):

    def __init__(self):
        super().__init__()

    def misturar(self):
        return f"Passando agua pressurizada pelo pó de cafe moido!"

    def servir(self):
        return f"Servindo em xicara pequena"
