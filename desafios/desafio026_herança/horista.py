from funcionario import Funcionario


class Horista(Funcionario):

    def __init__(self, nome, valor_hora, horas_trabalhadas):
        self.nome = nome
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def calcular_salario(self):
        desconto = (self.valor_hora * self.horas_trabalhadas) * self.INSS
        salario = (self.valor_hora * self.horas_trabalhadas) - desconto
        return salario
