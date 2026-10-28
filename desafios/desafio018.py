from rich import print
from rich.panel import Panel
from rich.traceback import install
from rich.text import Text

install()
class Churrasco:
    def __init__(self, nome_evento, quantidade_pessoas=0):
        self.nome_evento = nome_evento
        self.quantidade_pessoas = quantidade_pessoas

    def analisar(self):
        consumo_participante = 0.4
        preco_carne = 82.40
        recomendacao_compra = self.quantidade_pessoas * consumo_participante
        custo_total = recomendacao_compra * preco_carne
        custo_participante = custo_total / self.quantidade_pessoas

        conteudo = Text.from_markup(
            f"[white]Analisando[red] {self.nome_evento}[/] com [blue]{self.quantidade_pessoas} pessoas[/]\n"
            f"cada participante comerá [yellow]{consumo_participante}Kg[/] e cada Kg custa [red]R${preco_carne:,.2f}[/]\n"
            f"Recomendo comprar [yellow]{recomendacao_compra}Kg[/] de carne\n"
            f"o custo total será de [red]R${custo_total:,.2f}[/]\n"
            f"Cada pessoa pagará [red]R${custo_participante}[/]"
        )
        mostrar = Panel(
            conteudo,
            title=self.nome_evento,
            width=80,
        )

        print(mostrar)


c1 = Churrasco("Churras dos amigos", 15)
c1.analisar()
