from ui.form import formPessoaFisica,formPessoaJuridica, carregarPessoaCadastradas

def main():
    loop = True

    while loop:

        escolhar = int(input("1-Novo Cliente | 2-Lista Cliente | 3-Buscar Cliente: "))
        match escolhar:
            case 1:
                tipoCliente = int(input('Deseja cadastrar 1- Pessoa Fisica | 2- Pessoa Juridica'))
                if tipoCliente == 1:
                    formPessoaFisica()
                    print('Cliente registrado com sucesso!')
                elif tipoCliente == 2:
                    formPessoaJuridica()
                    print('Cliente registrado com sucesso!')
            case 2:
                carregarPessoaCadastradas()
            case 3:
                print('Aqui irei buscar')
            case _:
                print('Opção inválida!')            

        opcao = int(input('Deseja continuar o sistema? 1-Sim | 2-Nãp'))
        if(opcao == 2):
            loop = False


if __name__ == "__main__":
    main() 