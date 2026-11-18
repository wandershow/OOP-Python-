from funcionario import Funcionario


class Mensalista(Funcionario):

    def __init__(self, nome, salario_bruto):
        self.nome = nome
        self.salario_bruto = salario_bruto

    def calcular_salario(self):
        desconto = self.salario_bruto * self.INSS
        salario = self.salario_bruto - desconto
        return salario
