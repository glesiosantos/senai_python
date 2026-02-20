class Endereco:
    def __init__(self, logradouro, bairro, cidade, estado):
        self.logradouro = logradouro
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado

    def to_dict(self):
        return {
            "logradouro":self.logradouro,
            "bairro": self.bairro,
            "cidade": self.cidade,
            "estado": self.estado
        }    