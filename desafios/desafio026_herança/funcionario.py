from abc import ABC, abstractmethod


class Funcionario(ABC):

    SALARIO_MINIMO = 1612
    INSS = 0.075  # 7.5%

    def __init__(self, nome, salario_bruto):
        self.nome = nome
        self.salario_bruto = salario_bruto

    @abstractmethod
    def calcular_salario(self):
        pass

    def analisar_salario(self):
        qtd_salario_minimo = self.calcular_salario() / self.SALARIO_MINIMO
        print(
            f"O salario de {self.nome} ({type(self).__name__}) é de R${self.calcular_salario():.2f} e correspode a {qtd_salario_minimo:.1f} salarios minimos"
        )
