continuar = True
frutas = {}

while continuar:
    print('Selecione as opções abaixo:')
    print('1 - Add | 2 - Remover | 3 - Buscar')
    
    print('***** ****** ***** ***** **** ')
    opcao = int(input('Informe a opção: '))
    nomeFruta = ''
    valorFruta = 0.0

    match opcao:
        case 1:
            print('***** ****** ***** ***** **** ')
            nomeFruta = input('Informe o nome da fruta: ')
            valorFruta = float(input('Informe o preço da fruta: '))
            frutas.update({
                nomeFruta: valorFruta
            })
        case 2:
            print('***** ****** ***** ***** **** ')
            nomeFruta = input('Valor que deseja remover: ')
            del frutas[nomeFruta]
            print(f'A fruta removida foi {nomeFruta}')
        case 3:
            print('***** ****** ***** ***** **** ')
            nomeFruta = input('Informe nome para busca:')
            print(f'{frutas[nomeFruta]}')
        case _:
            print('***** ****** ***** ***** **** ')
            print('Opção invalida')

    opcao = int(input('Deseja continuar? 1-sim | 2-não '))

    if(opcao == 2):
        continuar = False
        print('Encerrando aplicação')

print('\n')
print('***** ****** ***** ***** **** ')
print(f'Resultado \n{frutas}')