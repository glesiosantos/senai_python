continuar = True
palavraChave = input('Informe uma palavra ').lower().strip()

digitadas = []
acertos = []
erros = 0

while continuar:

    senha = ""

    for letra in palavraChave:
        senha += letra if letra in acertos else "." 
        print(senha)

        if senha == palavraChave:
            print('Você acertou!')
            break
        tentativa = input('Digite uma letra: ').lower().strip()
        if tentativa in digitadas:
            print('Você ja digitou esta letra')
            continue
        else:
           digitadas += tentativa
           if tentativa in palavraChave:
               acertos += tentativa
           else:
               erros += 1
               print('Você errou!')
    print("X==:==\nX : ")
    print("X O " if erros >= 1 else "X")
    linha2 = ""
    if erros == 2:
        linha2 += " | "
    elif erros == 3:
        linha2 += " \| "
    elif erros >= 4:
        linha2 += " \|/ "

    print("X%s" % linha2)
    linha3 = ""

    if erros == 5:
        linha3 = " / "
    elif erros >= 6:
        linha3 = " / \"    
