menu = '''
--------------Menu------------

[1] Deposito
[2] Sacar
[3] Extrato
[0] Sair

Digite a opção: 
'''

saldo = 0
limite = 500
extrato = ''
numero_saque = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

    if opcao == '1':
        print('Depósito')
        valor = float(input('Valor a ser depositado: R$ '))
        if valor > 0:
            saldo += valor
            print(f'Você depositou R$ {valor:.2f}')
            extrato += f'+ R$ {valor:.2f}\n'
        else:
            print('Valor invalido!')
    elif opcao == '2':
        print('Saque')
        tira = float(input('Valor a sacar: R$ '))
        if tira > saldo:
            print('Saldo insuficiente.')
        elif tira <= saldo and tira <= 500.0:
            if numero_saque < LIMITE_SAQUE:
                saldo -= tira
                numero_saque += 1
                extrato += f'- R$ {tira:.2f}\n'
                print(f'Você sacou R$ {tira:.2f}')
            else:
                print('Você excedeu o limite de saque diário')
        elif tira > 500.0:
            print('R$500 é o valor máximo para saque!')

    elif opcao == '3':
        print('Extrato:')
        print('Não foram realizadas operações.' if not extrato else extrato)
        print(f'Saldo atual: R$ {saldo:.2f}')
    elif opcao == '0':
        break
    else:
        print('Opção invalida')