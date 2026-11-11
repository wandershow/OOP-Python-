from abc import ABC, abstractmethod


class Cafeteria(ABC):

    def __init__(self):
        super().__init__()

    def preparar(self):
        print(f"""_____INICIANDO O PREPARO_____
1. {self.ferver_agua()},
2. {self.misturar()},
3. {self.servir()}.
____BEBIDA PRONTA____""")

    def ferver_agua(self):
        return f"Fervendo a agua a 100° graus celcius"

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass
