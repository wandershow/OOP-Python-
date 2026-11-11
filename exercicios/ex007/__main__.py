from rich import print, inspect
from pessoa import Pessoa
from aluno import Aluno
from professor import Professor
from funcionario import Funcionario


def main():

    a1 = Aluno("Wanderson", 40, "TADS", "t25")
    a1.fazer_aniversario()
    a1.fazer_matricula()
    # inspect(a1, methods=True)

    p1 = Professor("Guanabara", 50, "TI", "DR.")
    p1.fazer_aniversario()
    p1.dar_aula()
    # inspect(p1, methods=True)

    f1 = Funcionario("Claudia", 27, "Secretaria", "Secretaria")
    f1.fazer_aniversario()
    f1.bater_ponto()
    # inspect(f1, methods=True)

    a1.estudar()
    p1.estudar()
    f1.estudar()


if __name__ == "__main__":
    main()
