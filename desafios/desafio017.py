from rich import print
from rich.panel import Panel
from rich.traceback import install
from rich.text import Text

install()


class Produto:

    def __init__(self, nome, preco=0):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        largura = len(self.nome) + 10
        linha = "-" * (largura - 6)
        conteudo = Text.from_markup(
            f"[white]{self.nome}\n{linha}\nR${self.preco:,.2f}",
            justify="center",
        )
        mostrar = Panel(
            conteudo,
            title="Produto",
            width=largura,
        )

        print(mostrar)


p1 = Produto("Iphone 17 Pro Max", 25_000.85)
p2 = Produto("Notebook Gamer", 8_000)

p1.etiqueta()
p2.etiqueta()
