from caminhao import Caminhao
from moto import Moto
from drone import Drone


def main():
    pedidos = [(Moto, 25), (Moto, 3), (Caminhao, 65), (Caminhao, 49), (Drone, 9), (Drone, 12)]

    for tipo, distancia in pedidos:
        try:
            veiculo = tipo(distancia)
            print(veiculo)
        except ValueError as erro:
            print(f"{tipo.__name__} para {distancia}km recusado: {erro}")


if __name__ == "__main__":
    main()
