from oo.models.cliente import Cliente
from oo.models.endereco import Endereco

def main():
    print('Inicializando Sistema')

    cliente = Cliente('Luiz','Neto')
    endereco = Endereco("Av. Sen. Alberto Silva, 1111", "São João","Teresina","PI")
    endereco2 = Endereco("Av. Petulia, 1200", "São Pedro","Teresina","PI")
    cliente.addEndereco(endereco)
    cliente.addEndereco(endereco2)

    cliente2 = Cliente('José', 'Filho')
    endereco3 = Endereco("Av. Dr. Pessoa, 5555", "Mocambinho","Teresina","PI")
    endereco4 = Endereco("Av. Teste, ", "São Pedro","Teresina","PI")

    cliente2.addEndereco(endereco3)
    cliente2.addEndereco(endereco4)

    # cliente3 = Cliente('Maria','Duarte')

    print(f'Nome cliente: {cliente.nomeCompleto()}')
    print(f'Enderecos: {cliente.visualizarEnderecos()}')

    print(f'Nome cliente: {cliente2.nomeCompleto()}')
    print(f'Enderecos: {cliente2.visualizarEnderecos()}')
    # print(f'Nome cliente: {cliente2.nomeCompleto()}')
    # print(f'Nome cliente: {cliente3.nomeCompleto()}')

if __name__ == "__main__":
    main() 