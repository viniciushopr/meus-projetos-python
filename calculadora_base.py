#C.C.B.N. Calculadora de Conversão de Bases Numéricas

numeros_hex = {10: 'A', 11 : 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

#Função para mostrar menu principal.
def menu1():
    print('=== Calculadora de Bases ===')
    print('1 - Decimal para')
    print('2 - Binário para')
    print('3 - Octal para')
    print('4 - Hexadecimal para')
    print('0 - Sair\n')

#Função para mostrar menu secundário.
def menu2():
    print('===============')
    print('1 - Decimal')
    print('2 - Binário')
    print('3 - Octal')
    print('4 - Hexadecimal\n')

# Função para converter de decimal para binário.
def dec_bin(num):
    restos = []
    while num > 0:
        resto = num%2
        num //= 2
        restos.insert(0, resto)
    num_bin = int(''.join(map(str, restos)))
    return num_bin

# Função para converter de decimal para octal.
def dec_oct(num):
    restos = []
    while num > 0:
        resto = num%8
        num //= 8
        restos.insert(0, resto)
    num_oct = int(''.join(map(str, restos)))
    return num_oct

# Função para converter de decimal para hexadecimal.
def dec_hex(num):
    restos = []
    while num > 0:
        resto = num%16
        num //= 16
        restos.insert(0, resto)
    for k, i in enumerate(restos):
        if i in numeros_hex:
            restos[k] = numeros_hex[i]
    num_hex = ''.join(map(str, restos))
    return num_hex

# Função para converter de binário para decimal.
def bin_dec(num):
    num = [int(i) for i in num]
    num.reverse()
    dec = 0
    for k, i in enumerate(num):
        dec += i * 2 ** k
    return dec

# Função para converter de ocral para decimal.
def oct_dec(num):
    num = [int(i) for i in num]
    num.reverse()
    dec = 0
    for k, i in enumerate(num):
        dec += i * 8 ** k
    return dec

# Função para converter de hexadecimal para decimal.
def hex_dec(num):
    num = [i for i in num]
    num.reverse()
    dec = 0
    for k, i in enumerate(num):
        if i in numeros_hex:
            dec += numeros_hex[i] * 16 ** k
        else:
            dec += int(i) * 16 ** k
    return dec

#------Código Principal------
while True:
    menu1()

    opcoes = ['Decimal para', 'Binário para', 'Octal para', 'Hexadecimal para']

    try:
        opcao1 = int(input('Digite um dos numeros para escolher umas das opcoes acima: ').strip())
        print()
    except ValueError:
        print("Opção inválida! Digite apenas números.\n")
        continue

    if opcao1 == 0:
        print('Saindo do sistema...\n')
        break

    else:
        print(f'Você escolheu a opcao {opcoes[opcao1-1]}.\n')

    menu2()

    try:
        opcao2 = int(input('Digite um dos numeros para escolher umas das opcoes acima: ').strip())
        print()
    except ValueError:
        print("Opção inválida! Digite apenas números.\n")
        continue

    print(f'Voce deseja converter de {opcoes[opcao1-1].split()[0]} para {opcoes[opcao2-1].split()[0]}\n')
    
    if opcao1 == opcao2:
        print('As bases sao identicas, nao a necessidade de conversao.\n')

    #DECIMAIS PARA OUTRAS
    elif opcao1 == 1 and opcao2 == 2:
        num = int(input('Digite o numero a ser convertido para binario: ').strip())
        print()
        print(f'O numero {num} virou {dec_bin(num)}\n')
        
    elif opcao1 == 1 and opcao2 == 3:
        num = int(input('Digite o numero a ser convertido para octal: ').strip())
        print()
        print(f'O numero {num} virou {dec_oct(num)}\n')

    elif opcao1 == 1 and opcao2 == 4:
        num = int(input('Digite o numero a ser convertido para hexadecimal: ').strip())
        print()
        print(f'O numero {num} virou {dec_hex(num)}\n')

    #BINARIAS PARA OUTRAS
    elif opcao1 == 2 and opcao2 == 1:
        num = input('Digite o numero a ser convertido para decimal: ').strip()
        print()
        print(f'O numero {num} virou {bin_dec(num)}\n')

    elif opcao1 == 2 and opcao2 == 3:
        num = input('Digite o numero a ser convertido para octal: ').strip()
        print()
        print(f'O numero {num} virou {dec_oct(bin_dec(num))}\n')

    elif opcao1 == 2 and opcao2 == 4:
        num = input('Digite o numero a ser convertido para hexadecimal: ').strip()
        print()
        print(f'O numero {num} virou {dec_hex(bin_dec(num))}\n')

    #OCTAIS PARA OUTRAS
    elif opcao1 == 3 and opcao2 == 1:
        num = input('Digite o numero a ser convertido para decimal: ').strip()
        print()
        print(f'O numero {num} virou {oct_dec(num)}\n')

    elif opcao1 == 3 and opcao2 == 2:
        num = input('Digite o numero a ser convertido para binario: ').strip()
        print()
        print(f'O numero {num} virou {dec_bin(oct_dec(num))}\n')

    elif opcao1 == 3 and opcao2 == 4:
        num = input('Digite o numero a ser convertido para hexadecimal: ').strip()
        print()
        print(f'O numero {num} virou {dec_hex(oct_dec(num))}\n')

    #HEXADECIMAIS PARA OUTRAS
    elif opcao1 == 4 and opcao2 == 1:
        num = input('Digite o numero a ser convertido para decimal: ').upper()
        print()
        print(f'O numero {num} virou {hex_dec(num)}\n')

    elif opcao1 == 4 and opcao2 == 2:
        num = input('Digite o numero a ser convertido para binario: ').upper()
        print()
        print(f'O numero {num} virou {dec_bin(hex_dec(num))}\n')

    elif opcao1 == 4 and opcao2 == 3:
        num = input('Digite o numero a ser convertido para octal: ').upper()
        print()
        print(f'O numero {num} virou {dec_oct(hex_dec(num))}\n')


print('Obrigado por utilizar meu progama!')