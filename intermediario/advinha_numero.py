import random

numeroAleatorio = random.randint(1,10)

def compararDoisValores(a, b):
    return a == b

def daResultado():
    if compararDoisValores(numeroAleatorio, numero):
        print('Acertou danado!')
    else:
        print('Errou!')

numero = int(input('Informe um numero entre 1 a 10: '))

print(daResultado())
print(type(daResultado()))

