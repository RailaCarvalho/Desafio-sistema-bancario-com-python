menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido! O valor do depósito deve ser positivo.")

    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            valor = float(input("Informe o valor do saque: "))
            if valor > saldo:
                print("Saldo insuficiente para realizar o saque.")
            elif valor > limite:
                print("O valor do saque excede o limite de R$ 500,00 por saque.")
            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("Valor inválido! O valor do saque deve ser positivo.")
        else:
            print("Você atingiu o limite de saques diários (3 saques).")

    elif opcao == "e":
        print("\n=========== EXTRATO ===========")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("===============================")

    elif opcao == "q":
        print("Saindo do sistema...")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")