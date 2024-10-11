# Listas para armazenar usuários e contas
usuarios = []
contas = []

# Função para depósito (positional only)
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

# Função para saque (keyword only)
def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato, numero_saques

# Função para extrato (positional and keyword only)
def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

# Função para cadastrar usuário
def cadastrar_usuario(nome, data_nascimento, cpf, endereco):
    # Verifica se o CPF já está cadastrado
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("Usuário com esse CPF já cadastrado!")
        return
    
    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")

# Função para cadastrar conta corrente
def criar_conta(cpf):
    usuario = buscar_usuario_por_cpf(cpf)
    if usuario:
        numero_conta = len(contas) + 1
        conta = {
            "agencia": "0001",
            "numero_conta": numero_conta,
            "usuario": usuario
        }
        contas.append(conta)
        print(f"Conta {numero_conta} criada com sucesso para o usuário {usuario['nome']}")
    else:
        print("Usuário não encontrado. Conta não criada.")

# Função para buscar usuário pelo CPF
def buscar_usuario_por_cpf(cpf):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return usuario
    return None

# Função para listar contas
def listar_contas():
    if contas:
        print("\n========== LISTA DE CONTAS ============")
        for conta in contas:
            print(f"Agência: {conta['agencia']}, Número da Conta: {conta['numero_conta']}, Titular: {conta['usuario']['nome']}")
        print("=======================================")
    else:
        print("Nenhuma conta cadastrada.")

# Função principal com menu
def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        menu = """
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [nu] Novo Usuário
        [nc] Nova Conta
        [lc] Listar Contas
        [q] Sair

        => """
        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                LIMITE_SAQUES=LIMITE_SAQUES
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            nome = input("Nome: ")
            data_nascimento = input("Data de Nascimento (dd/mm/aaaa): ")
            cpf = input("CPF (somente números): ")
            endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla estado): ")
            cadastrar_usuario(nome, data_nascimento, cpf, endereco)

        elif opcao == "nc":
            cpf = input("Informe o CPF do usuário: ")
            criar_conta(cpf)

        elif opcao == "lc":
            listar_contas()

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

# Executa o sistema
main()
