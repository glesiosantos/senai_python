from models.conta import Conta

class ContaCorrente(Conta):
    def __init__(self,numero, titular, taxa):
        super().__init__(numero, titular)
        self.taxa = taxa

    def sacar(self, valor):
        total = valor + self.taxa
        return super().sacar(total)

    def visualizarDadosConta(self):
        return super().visualizarDadosConta()   
