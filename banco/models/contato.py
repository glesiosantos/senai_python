class Contato:
    def __init__(self, ddd, numero):
        self.ddd = ddd,
        self.numero = numero 

    def to_dict(self):
        return {
            "ddd": self.ddd,
            "numero": self.numero
        }    