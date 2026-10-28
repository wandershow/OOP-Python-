from rich import print
from rich.panel import Panel
from rich.traceback import install
from rich.text import Text

install()


class Gamer:
    def __init__(self, nome, nick_name):
        self.nome = nome
        self.nick_name = nick_name
        self.favoritos = []

    def add_favoritos(self, jogo):
        self.favoritos.append(jogo)

    def ficha(self):

        texto = f"[white]Nome Real:[/] [bold blue on black]{self.nome}[/]\n"
        texto += f"[blue]Jogos Favoritos[/]\n"
        for jogo in sorted(self.favoritos):
            texto += f":zombie: -  {jogo}\n"
        conteudo = Text.from_markup(texto)

        mostrar = Panel(
            conteudo,
            title=f"jogador - {self.nick_name}",
            width=60,
        )

        print(mostrar)


j1 = Gamer("Wanderson da Silva", "Neo_RG")
j1.add_favoritos("Fifa.")
j1.add_favoritos("GTA 6")
j1.add_favoritos("Comand & Coquer")
j1.add_favoritos("The Sims")

j1.ficha()

j2 = Gamer("Maria Flor", "Florzinha")
j2.add_favoritos("Roblox")
j2.add_favoritos("Mortal Kombat")

j2.ficha()
