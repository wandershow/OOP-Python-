# declaração de Classe
class Gafanhoto:
    """
    classe Gafanhoto
    recebe nome e idade como atributos
    """

    def __init__(self, nome="vazio", idade=0):  # Método Construtor
        # Atributos de Instância
        self.nome = nome
        self.idade = idade

    # Metodos de Instância
    def aniversario(self):
        self.idade += 1

    def __str__(self):
        return f"{self.nome} é Gafanhoto e tem {self.idade} anos de idade"

    def __getstate__(self):
        return f"{self.nome} é Gafanhoto e tem {self.idade} anos de idade"


# Declaração de Objetos
g1 = Gafanhoto("Maria", 17)  # instanciação de objeto
g1.aniversario()
# print(g1)

print(g1.__dict__)  # Dunder Attribute
print(g1.__getstate__())  # Dunder Method
print(g1.__class__)  # Dunder Atribute
print(g1.__doc__)  # Dunder Attribute
