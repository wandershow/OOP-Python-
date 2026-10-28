"""
Crie uma classe Funcionario, onde podemos cadastrar nome, setor e cargo.
Crie tambem um método que permita ao funcionario se aposentar
"""


class Funcionario:

    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def aposentar(self):
        print(
            f"O funcionario {self.nome}, do setor {self.setor}, cargo {self.cargo} se aposentou!"
        )

    def __str__(self):
        return f"Funcionario {self.nome}, trabalha no setor {self.setor} e é nosso {self.cargo} "


f1 = Funcionario("Paulo", "Logistica", "Motorista")

print(f1)
f1.aposentar()
