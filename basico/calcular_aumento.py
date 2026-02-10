salario = float(input('Informe um salario:'))
porcentagem = float(input('Informe a porcentagem de aumento: '))
resultado = salario + (salario * (porcentagem / 100))
print(f'O novo salario será {resultado:.2f}')

