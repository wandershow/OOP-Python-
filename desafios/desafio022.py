from rich import print
from rich.panel import Panel
from rich.traceback import install
from rich.text import Text
from rich.console import Console

console = Console()

install()


class Televisao:

    def __init__(self, total_canais=5, volume_maximo=5):
        self.ligada = False
        self.canal = 1
        self.total_canais = total_canais
        self.volume = 1
        self.volume_maximo = volume_maximo

    def ligar_desligar(self):
        self.ligada = not self.ligada
        if self.ligada:
            print("TV ligada!")
            print(self.ficha())
        else:
            print("TV desligada!")

    def aumentar_volume(self):
        if not self.ligada:
            print("Ligue a TV primeiro!")
            return
        self.volume += 1
        if self.volume > self.volume_maximo:
            self.volume = self.volume_maximo
            print("Volume Maximo")
        print(self.ficha())

    def diminuir_volume(self):
        if not self.ligada:
            print("Ligue a TV primeiro!")
            return
        self.volume -= 1
        if self.volume < 1:
            self.volume = 1
            print("Volume minimo")
        print(self.ficha())

    def proximo_canal(self):
        if not self.ligada:
            print("Ligue a TV primeiro!")
            return
        self.canal += 1
        if self.canal > self.total_canais:
            self.canal = 1
        print(self.ficha())

    def canal_anterior(self):
        if not self.ligada:
            print("Ligue a TV primeiro!")
            return
        self.canal -= 1
        if self.canal < 1:
            self.canal = self.total_canais
        print(self.ficha())

    def ficha(self):

        texto = f"[white]Canal:[/] [bold blue on black]{self.canal}[/]\n"
        texto += f"[white]Volume:[/] [bold blue on black]{self.volume}[/]"
        return Panel(
            Text.from_markup(texto),
            title=f"TV",
            width=60,
        )


if __name__ == "__main__":
    tv = Televisao()
    comandos = "Comandos: @ liga/desliga | < > canal | - + volume | 0 sair"
    print(comandos)

    while True:
        opcao = input("> ").strip()
        console.clear()  # apaga a tela antes de mostrar o resultado
        print(comandos)
        if opcao == "0":
            break
        elif opcao == "@":
            tv.ligar_desligar()
        elif opcao == ">":
            tv.proximo_canal()
        elif opcao == "<":
            tv.canal_anterior()
        elif opcao == "+":
            tv.aumentar_volume()
        elif opcao == "-":
            tv.diminuir_volume()
        else:
            print("Comando inválido!")

    print("Até mais!")
