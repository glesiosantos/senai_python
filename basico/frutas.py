continuar = True
lista = []

while continuar:
    fruta = input('Informe uma fruta:')
    lista.append(fruta.strip())

    desejaContinuar = input('Deseja continar? Sim (S) | Não (N)')

    if(desejaContinuar.strip().lower() == 'n' or 
       desejaContinuar.strip().lower() == 'nao' or
       desejaContinuar.strip().lower() == 'não') :
        continuar = False

print(f'A frutas informadas:\n{lista}')