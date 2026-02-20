from models.conta import Conta
from models.pessoa import Pessoa
from models.corrente import ContaCorrente
from models.endereco import Endereco
from models.contato import Contato

def main():

    endereco = Endereco('Rua das Saudades, 1550', 'São João', 'Teresina', 'PI')
    contato1 = Contato(86, '98866.5522')
    contato2 = Contato(86, '98899.6669')

    maria= Pessoa('Maria Joaquina', endereco)
    mariaConta = ContaCorrente(2, maria)
    mariaConta.depositar(1000)
    maria.add_contato(contato1)
    maria.add_contato(contato2)

    mariaConta.salvar_conta()

    endereco2 = Endereco('Rua das Liberdade, 250', 'São Pedro', 'Teresina', 'PI')
    contato3 = Contato(86, '98877.5522')
    contato4 = Contato(86, '98855.6669')

    carlos= Pessoa('Carlos Antônio', endereco2)
    carlosConta = ContaCorrente(3, carlos)
    carlosConta.depositar(1000)
    carlos.add_contato(contato3)
    carlos.add_contato(contato4)

    carlosConta.salvar_conta()

if __name__ == "__main__":
    main()