from cafeteria import Cafeteria


class Cha(Cafeteria):

    def __init__(self):
        super().__init__()

    def misturar(self):
        return f"Mergulhando o sache de ervas na agua"

    def servir(self):
        return f"Servindo na caneca de porcelana com limão"
