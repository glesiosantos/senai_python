from models.cliente import Cliente

def menu():
    print("\n" + "="*30)
    print("      SISTEMA DE VENDAS")
    print("="*30)
    print("1. Cadastrar Cliente")
    print("2. Cadastrar Produto")
    print("3. Realizar Venda")
    print("0. Sair")
    return input("\nEscolha uma opção: ")

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
                print('Cadastrar produto')                
            case '3':
                print('Realizar Venda')
            case '0':
                print('Sair do sistema')
                continuar = False                
            case _ :     
                print('Opções validas')

if __name__ ==  '__main__':
    main()