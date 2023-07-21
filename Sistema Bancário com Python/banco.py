import os
saldo = 0
limite = 500
extrato = []
numero_saques = 0

while True:
    menu = str(input(""""

    ############ MENU ############

    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [4] - Sair

    ##############################
    >>: 
"""))

    if menu == '1':
        deposito = float(input("Digite o valor do depósito: "))
        if deposito >= 0:
            saldo += deposito
            print(f'Valor depositado: R${saldo:.2f}')
            extrato.append(f'D: R$ {deposito:.2f}')

        elif deposito < 0:
            print('Digite um valor inteiro positivo')

    elif menu == '2':
        while True:
            saque = float(input("Digite o valor que queira sacar: "))
            
            if numero_saques >= 3:
                os.system("cls")
                print('Número de saque diários já realizados: 3')
                break

            elif saque > limite:
                os.system("cls")
                print('Seu limite de saque é de até R$500.00 conto')
                break

            elif saldo < saque:
                os.system("cls")
                print("Boca aberta tu não tem saldo!!")
                break
            elif saque > limite:
                print("Valor sacado não suportado, digite um valor abaixo ou igual a R$500.00 reais")

            elif saldo > saque:
                numero_saques += 1
                saldo -= saque
                print(f"""
Valor sacado com sucesso: R$ {saque:.2f}
Seu saldo atual é de: R$ {saldo:.2f}
                       """)
                extrato.append(f'S: R$ {saque:.2f}')
                break

    elif menu == '3':
        os.system('cls')

        if extrato == []:
            print("Não foram feitas movimentações hoje.")

        print("Extrato")
        for i in extrato:
            print(i)
        print(f"Seu saldo atual é: R$ {saldo:.2f}")

    elif menu == '4':
        break

    else:
        print("Operação inválida, digite um número ai boca aberta!")
