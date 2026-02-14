from models.conta import Conta
from models.corrente import ContaCorrente

def main():

    maria = Conta(1,"Maria Alves")
    maria.depositar(100)
    maria.depositar(150)

    joao = ContaCorrente(2, "João da Costa", 0.05)
    maria.tranferir(100, joao)

    tete = ContaCorrente(3, "Maria Tetê", 0.05)

    joao.depositar(1000)
    joao.tranferir(200, tete)

    print('*'*10)
    print(f'{maria.visualizarDadosConta()}')
    print('*'*10)
    print(f'{joao.visualizarDadosConta()}')
    print('*'*10)
    print(f'{tete.visualizarDadosConta()}')

if __name__ == "__main__":
    main()