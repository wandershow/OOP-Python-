from rich.traceback import install  # mostra os erros formatados e simplificados para se entender

install()


def divisao(x, y):
    return x / y


print(divisao(50, 2))
print(divisao(50, 0)) #Aqui mostra o erro formatado
