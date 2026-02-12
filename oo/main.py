from models.veiculo import Veiculo

def main():
    print('Inicializando Sistema')
    list = []
    carroByd = Veiculo(2026, 'BYD', 4)
    motoHonda = Veiculo(2026, 'Honda Motos', 2)
    list.append(carroByd)
    list.append(motoHonda)

    for v in list:
        print(f'{v.marca}')

if __name__ == "__main__":
    main() 