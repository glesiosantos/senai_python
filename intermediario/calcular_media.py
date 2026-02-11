contador = 0
notas = []

def media(lista):
    total = 0
    for i in lista:
        total = total + i
    return total / len(lista)

while contador < 3:
    nota = float(input(f'Informe a nota {contador + 1}: '))
    notas.append(nota)
    contador += 1

print(f'Notas: {notas}')

resultado = media(notas)
print(f'resultado: {resultado}')