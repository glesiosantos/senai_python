from cliente import Cliente
from endereco import Endereco

def main():
    print('Inicializando Sistema')

    cliente = Cliente('Luiz','Neto', 5)
    cliente2 = Cliente('José', 'Filho')
    cliente3 = Cliente('Maria','Duarte')

    print(f'Nome cliente: {cliente.nomeCompleto()}')
    print(f'Nome cliente: {cliente2.nomeCompleto()}')
    print(f'Nome cliente: {cliente3.nomeCompleto()}')

if __name__ == "__main__":
    main() 