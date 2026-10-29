from rich import print
from rich.traceback import install

install()


class Caneta:
    def __init__(self, cor):
        self.cor = cor.lower().strip()
        self.tampada = True
        if self.cor == "azul":
            self.cor = "blue"
        elif self.cor in ("vermelho", "vermelha"):
            self.cor = "red"
        else:
            self.cor = "green"

    def destampar(self):
        self.tampada = False

    def escrever(self, texto):
        self.texto = texto

        cor = f"{self.cor.lower()}"
        if self.tampada == True:
            print("Você precisa destampar a caneta!")
            return
        print(f"[{cor}]{texto}")

    def quebrar_linha(self, quantidade=1):
        for _ in range(quantidade):
            print()


c1 = Caneta("Azul")
c2 = Caneta("Vermelha")
c3 = Caneta("verde")

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever("Ola, tudo bem? ")
c1.quebrar_linha(2)
c2.escrever("Ola, Gafanhoto! ")
c3.escrever("Vamos exercitar!")
