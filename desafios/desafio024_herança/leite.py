from cafeteria import Cafeteria


class Leite(Cafeteria):

    def __init__(self):
        super().__init__()

    def misturar(self):
        return f"Passando vapor pressurizado pelo bico de leite"

    def servir(self):
        return f"Servindo na caneca grande ja com Café"
