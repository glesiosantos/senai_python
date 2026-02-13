class Veiculo:
    def __init__(self, ano: int, marca: str, numeroPneus: int):
        self.ano = ano
        self.marca = marca
        self.numeroPneus = numeroPneus  

    def mostrarVeiculo(self):
        return f'Marca: {self.marca}\nAno: {self.ano}'          
