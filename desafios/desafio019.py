class Livro:
    def __init__(self, titulo, quantidade_paginas):
        self.titulo = titulo
        self.quantidade_paginas = quantidade_paginas
        self.pagina = 0

    def avancar(self, quantidade_avancar):
        for _ in range(quantidade_avancar):
            if self.pagina == self.quantidade_paginas:
                print("Você chegou ao fim do livro!")
                break
            self.pagina += 1
            print(f"Página {self.pagina}")

    def __str__(self):
        return f"Você acabou de abrir o livro {self.titulo} que tem {self.quantidade_paginas} paginas"


l1 = Livro("10 coisas que eu aprendi", 20)
l1.avancar(5)
l1.avancar(10)
l1.avancar(100)
