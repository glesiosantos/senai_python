from models.cliente import Cliente
from models.produto import Produto

def menu():
    print("\n" + "="*30)
    print("      SISTEMA DE VENDAS")
    print("="*30)
    print("1. Cadastrar Cliente")
    print("2. Cadastrar Produto")
    print("3. Realizar Venda")
    print("4. Listar clientes")
    print("0. Sair")
    return input("\nEscolha uma opção: ")

def listar_clientes():
    with open('clientes.txt', 'r') as f:
        for linha in f:
            dados = linha.strip().split(';')
            print(f'{dados[0]} - {dados[1]}')

def listar_produtos():
    with open('produtos.txt', 'r') as f:
        for linha in f:
            dados = linha.strip().split(';')
            print(f'{dados[0]} - {dados[1]} - {dados[2]}')             

def main():
    continuar = True

    while(continuar):
        opcao = menu()

        match opcao:
            case '1':
                cpf = input('Informe CPF: ')
                nome = input('Informe nome: ')
                cliente = Cliente(cpf, nome)
                cliente.salvar()                
            case '2':
                codigo = int(input('Informe um código: '))
                descricao = input('Informe nome do produto: ')
                valor = float(input('Informe valor do produto: '))
                produto = Produto(codigo, descricao,valor)
                produto.salvar()                
            case '3':
                print('Realizar Venda')
            case '4':
                listar_clientes()
            case '0':
                print('Sair do sistema')
                continuar = False                
            case _ :     
                print('Opções validas')

if __name__ ==  '__main__':
    main()