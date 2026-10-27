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
        
