from cliente import Cliente
from endereco import Endereco

def main():
    print('Inicializando Sistema')

    endereco = Endereco("Av. Sen. Alberto Silva, 1111", "São João","Teresina","PI")
    cliente = Cliente('Luiz','Neto')
    
    # cliente2 = Cliente('José', 'Filho')
    # cliente3 = Cliente('Maria','Duarte')

    print(f'Nome cliente: {cliente.nomeCompleto()}')
    print(f'Endereco: {cliente.endereco.enderecoCompleto()}')
    # print(f'Nome cliente: {cliente2.nomeCompleto()}')
    # print(f'Nome cliente: {cliente3.nomeCompleto()}')

if __name__ == "__main__":
    main() 