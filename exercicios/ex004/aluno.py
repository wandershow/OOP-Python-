from pessoa import Pessoa

class Aluno(Pessoa):  # HERANÇA
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.truma = turma

    def fazer_matricula(self):
        print(f"O Aluno {self.nome} fez a matricula!")
