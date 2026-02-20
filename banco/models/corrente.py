from models.conta import Conta

class ContaCorrente(Conta):
    def __init__(self, numero, pessoa):
        super().__init__(numero, pessoa)
        self.limite = 500

    def sacar(self, valor):
        total_disponivel = self._saldo + self.limite

        if total_disponivel >= valor:
            self._saldo -= valor
            return True
        else:
            print(f'Saldo insuficiente! Disponível: {total_disponivel:.2f}')
            return False